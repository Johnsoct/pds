package utility

import (
	"testing"
)

type testCase struct {
	input  string
	output bool
}

func TestGetDisallowedDangerousCharactersRegex(t *testing.T) {
	regex := GetDisallowedDangerousCharactersRegex()
	tests := []testCase{
		{input: "", output: false},
		{input: "safe", output: false},
		{input: "ssafesafesafesafesafesafesafesafesafesafesafesafesafesafesafeafe", output: false},
		{input: "unsafe*", output: true},
		{input: "&&*", output: true},
		{input: "((", output: true},
		{input: "(start*and*end(", output: true},
	}

	for _, v := range DISALLOWED_INPUTS {
		tests = append(tests, testCase{input: v, output: true})
	}

	for _, v := range tests {
		t.Run(
			"Cases: "+v.input,
			func(t *testing.T) {
				if regex.MatchString(v.input) != v.output {
					t.Errorf("Input, %s, did not match as expected, %t", v.input, v.output)
				}
			},
		)
	}
}
