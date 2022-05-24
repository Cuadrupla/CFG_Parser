# CFG_Parser
Lab.5 - Context Free Grammar Parser

To run either of the file check the -h section of them in short to run the cfg_validation_engine.py you should run:

```
python3 cfg_validation_engine.py cfg_config_file.txt
```

# The input format
Regarding the input format, we will aproach the exact same form as the previous projects having the following changes:
- Non-terminals represents the starting point for the non-terminals variables
- Terminals represents the starting point for the terminals variables
- Rules represents the starting point for the productions
- Start represents the starting point for the start variable;

Conventions:
1. All non-terminal variables are uppercase/capital letter;
2. All terminal varaibles are lowercase letter
3. All procedures are constructed in the following format: <Non-terminal letter>/<"~"(empty string)|<every possible combination of terminals and non-terminals>>
