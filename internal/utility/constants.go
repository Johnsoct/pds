package utility

var (
	CONFIRMATIONS = []string{
		"y", "yes", "n", "no",
	}
	DISALLOWED_INPUTS = []string{
		";", "&&", "||", "|", "(", ")", "`", ">", ">>", "<", "*", "?", "~", "$", ",", "%",
	}
	FREQUENCIES = []string{
		"never", "bi-monthly", "bi-weekly", "monthly", "weekly", "yearly",
	}
)
