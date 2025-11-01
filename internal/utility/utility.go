package utility

import (
	"regexp"
	"strings"
)

// GetDisallowedDangerousCharactersRegex returns a RegExp based on
// `regexp.MustCompile` utilizing regex alternations.
//
// Matches specific character patterns NOT classes.
func GetDisallowedDangerousCharactersRegex() *regexp.Regexp {
	patterns := []string{}

	for _, v := range DISALLOWED_INPUTS {
		var escapedChars []string

		// Some inputs contain more than one char and need individually escaped
		for _, char := range v {
			escapedChars = append(escapedChars, "\\"+string(char))
		}

		patterns = append(patterns, strings.Join(escapedChars, ""))
	}

	return regexp.MustCompile(strings.Join(patterns, "|"))
}
