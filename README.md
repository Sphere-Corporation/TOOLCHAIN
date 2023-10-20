# CONVERT
A tool to convert from an assembled 6800 code to several Sphere-1 compatible formats

# Installation

## Prerequisites
 
 * Install `Python 3.x` - versions above 3.9 are currently supported
 * Install "click" by typing `pip3 install click`


## convertEXE package

 * Clone the repository and ensure that the path is on your search path.
 * Test the installation by typing 
 `convertEXE --version`
 * If you see the following: 
 `convertEXE (Version 1.0.1): Convert MC6800 assembled code into Sphere-1 loadable package and other formats.` then all is well.
 * If not, check that the repository is cloned correctly and that the location is definitely on your search path.

# Formats supported

 * Virtual Cassette for Ben Zotto's Virtual Sphere-1 emulator
 * .WAV file for storing as a "true' cassette audio file

# How to use

```
Usage: convertEXE [OPTIONS]

Options:
  -b, --base TEXT      Base address.  [required]
  -c, --cassette TEXT  Cassette output file.
  -i, --input TEXT     Input MC6800 executable file.  [required]
  -n, --noheader       Don't produce headers for JS file.
  -o, --output TEXT    Output file (will have a '.js' extension).
  -p, --prefix TEXT    Cassette prefix.
  -t, --title TEXT     Cassette title (for Virtual Sphere).
  -s, --silent         Silent (no output).
  --version            Show the version and exit.
  --help               Show this message and exit.
  ```