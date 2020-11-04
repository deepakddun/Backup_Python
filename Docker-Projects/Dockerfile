FROM alpine:latest AS builder
RUN echo "Hello There " > build.txt

FROM alpine:latest AS tester
COPY --from=builder build.txt build.txt
RUN echo "MY NAME IS DEEPAK " >> build.txt

FROM alpine:latest AS packaging
COPY --from=tester build.txt build1.txt
CMD cat build1.txt