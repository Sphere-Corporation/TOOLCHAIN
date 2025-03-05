# TOOLCHAIN
A set of tools to convert from various SPHERE-1 formats to other SPHERE-1 formats.

These comprise:
<table border="0">
    <tr>
        <td><tt><b>build</td>
        <td>A tool to control a complete build from commencement to completion (including coordinating the other tools listed here).</td>
    </tr>
    <tr>
        <td><tt><b>convertEXE</td>
        <td>Converts assembled 6800 code to several Sphere-1 compatible formats.
    </td>
    </tr>
    <tr>
        <td><tt><b>convertROM</td>
        <td>Converts a raw binary SPHERE-1 ROM image to an ORB-compatible format.
    </td>
    </tr>
    <tr>
        <td><tt><b>bin2sphere</td>
        <td>A utility for producing vintage Sphere cassette tape data blocks.
    </td>
    </tr>
</table>

# Installation

## Prerequisites (for the full tool set)
 
 * Install `Python 3.x` - versions above 3.9 are currently supported
 * Install "[click](https://palletsprojects.com/p/click/)" by typing `pip3 install click`
 * Install `bin2sphere`
    * Clone [Ben Zotto's bin2sphere](https://github.com/bzotto/bin2sphere) repository
    * Folow the build instructions in the [README](https://github.com/bzotto/bin2sphere/blob/main/README.md)
    * Ensure the built executable is located in the same folder/directory as the `convertEXE` from this repo
  * Install `srec2bin`
    * Source code is included for v1.1
    * Ensure the built executable is located in the same folder/directory as the `convertEXE` from this repo

> **_NOTE:_**  
_There is a version of `bin2sphere` included in this repo is dated October 9th 2023. It is recommended that to ensure the latest software is being used that you follow the installation instructions for `bin2sphere` above._
>
>_There is a version of `srec2bin` included in this repo(compiled for Apple silicon) is dated April 2nd 2010. It is recommended that to ensure the latest software is being used that you check the [here](http://www.dragonwins.com/domains/getteched/rfid/srec2bin/index.htm) to ensure you have the latest version. Should you need/wish to compile the software, you will need a C compiler. The source code for v1.1 is included._ 
>
>_Within the conversion tools, there is a library written by David Beazley [http://www.dabeaz.com](http://www.dabeaz.com) which converts a binary file to Kansas City Cassette format as used by the Sphere-1. (Original script available on [his site](http://www.dabeaz.com/py-kcs/index.html)).This has been updated by Ben Zotto in 2023 and again by Andrew Shapton also in 2023. The Python source code is required._

## convertEXE package

 * Clone the repository and ensure that the path is on your search path.
 * Test the installation by typing 
 `convertEXE --version`
 * If you see the following: 

 `convertEXE (Version 1.0.3): Convert MC6800 assembled code into Sphere-1 loadable package and other formats.` 

`(c) Andrew Shapton 2023, Portions (c) Ben Zotto 2023` all is well.

**OR**

`convertROM --version`

If you see the following:

`convertROM (Version 1.2): 
Converts a Sphere ROM binary file into a form suitable for the SPHERE-Firmware emulator`

 Note that the versions *could* be slightly different from these shown, if small bugfixes have been introduced.
 
 If not, check that the repository is cloned correctly and that the location is definitely on your search path.

# convertEXE
## Formats supported

 * Virtual Cassette for Ben Zotto's Virtual Sphere-1 emulator
 * Javascript for manually embedding into the Virtual Sphere-1 emulator
 * Virtual Cassette "V2" format for automatically embedding into the Virtual Sphere-1 emulator (experimental)
 * .WAV file for storing as a "true' cassette audio file

## How to use

```
Usage: convertEXE [OPTIONS]

Options:
  -b, --base TEXT      Base address.  [required]
  -c, --cassette TEXT  Cassette output file.
  -I, --in TEXT        Specify an input folder.  [required]
  -i, --input TEXT     Input MC6800 executable file.  [required]
  -j, --js TEXT        Virtual Cassette Javascript (will have a '.js'
                       extension).
  -m, --movebin        Move original binary to output location
  -n, --noheader       Don't produce headers for JS file.
  -O, --out TEXT       Specify an output folder.  [required]
  -p, --prefix TEXT    Cassette prefix.
  -s, --silent         Silent (no output).
  -t, --title TEXT     Cassette title (for Virtual Sphere).
  -v, --vcass TEXT     Produce a virtual cassette in V1 format.
  -v2, --vcass2 TEXT   Produce a virtual cassette in V2 format.
  --version            Show the version and exit.
  --help               Show this message and exit.

  Check out the Github page for more documentation at
  https://github.com/Sphere-Corporation/CONVERT

  ```

# convertROM
## Explanation

Converts a raw, SPHERE-1 ROM Image into a format that can be used with either:
- a Project ORB ROM Emulator
- [Ben Zotto's Virtual SPHERE-1](https://sphere.computer/emulator/)

## How to use
```
Usage: convertROM [OPTIONS]

Options:
  -i, --input TEXT    Specify a SPHERE-1 ROM file.  [required]
  -o, --output TEXT   Specify an output file.
  -f, --format TEXT   Specify the output format. (required)
  -e, --ext TEXT      Extension for output file.
  -b, --base TEXT     Base address of ROM.
  -c, --comment TEXT  < 80 characters of comment for the ROM image (in
                      quotes).
  -s, --silent        Silent (no output).
  -l, --license       Show the license (MIT).
  -v, --version       Show the version.
  --help              Show this message and exit.

  ```

  Defaults:
  
  | Argument  | Value  |Notes|
  |-----------|--------|-----|
  |`ext`      |  `.h`  |Extension given to the output file if no other extension is given|
  |`base`     | `0xFE00`| Location of the base address of the ROM Image|
