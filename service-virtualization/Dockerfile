FROM bbyars/mountebank:2.9.1
COPY /templates /templates
ENTRYPOINT ["/usr/bin/env"]
CMD ["mb","--configfile","/templates/imposters.ejs"]
