quotegen
===========

Generate a random quote based on the list of available quotes


Prerequesites
----------------
quotegen runs in python3.9 and above. It does not require any further depedencies. 


Installation
--------------

Installation is done using the uv toolchain. Build and install with:

```bash
uv build
uv tool install
```

Check if the code is installed correctly by running

```bash
quote_gen --version
```

If it prints the version, then the quotegen is installed successfully.

Usage
-------

Run the command:

```bash
quote_gen
```

Adding a quote
---------------
To add a quote, open the quotes.json file located at ~/.quote_gen/quotes.json (or in the project path) and add a JSON object with "quote" and "author" fields. Example entry:

```json
{
  "quote": "Your quote here",
  "author": "Author Name"
}
```

Save the file; new quotes will be used the next time you run quote_gen.



Support
--------

For any bugs, queries or issues, please raise an issue in github or contact me at sramsubu@gmail.com.


Licence
--------

The project is licensed under GPL v3. Please read the LICENSE file for further details


