# Automated API Testing

## Goals ##
To experiment with:
- Service virtualization
- Automated regression testing of APIs that accounts for whole process

## TODOs ##
- ~~Setup mountebank~~
- ~~Setup pytest with tavern, JSON only~~
- ~~Setup XML validation (might need new plugin)~~
- ~~'Dynamic' testing that checks downstream systems based on XML values~~
- ~~'Static' testing that checks all results based on predefined values~~
- ~~External files in tests instead of inline~~
- Figure out dynamic checking of things like string months to their integer equivalent (using fixtures maybe?)
- Separate out tests to run dev/prod tests separately
- Better way to manage ports?
- Validate XML with external file
- Setup actual ports (at least for prod?)
- Optimize mountebank templates, without so many ports/externalized files
- More downstream systems

# Running

Refer to the github workflow for commands to run to start and stop the docker container and run the tests.