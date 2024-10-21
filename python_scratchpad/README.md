# Live Coding Scratchpad

I use this directory to do live coding tests in Python. To setup run _either_ of
the following for a dockerized or bare metal setup:

```bash
make -f Makefile.docker setup
# OR
make -f Makefile.local setup
```

You can then run the application with:

```bash
make
```

Further functionality is available as needed:

```bash
make lint
make types
make test
```
