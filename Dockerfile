FROM mcr.microsoft.com/windows-cssc/python3.7windows:ltsc2019

WORKDIR /Project

LABEL maintainer="mmd17003@student.mdu.se"

RUN echo "Fetching repositories..."
RUN curl.exe -SLo trace_tool.zip https://github.com/enxhiferko/TraceAnalyser/archive/refs/heads/main.zip
RUN tar -xf trace_tool.zip

RUN curl.exe -SLo pipeline.zip https://github.com/MarcusM94/CI-CD_Pipeline/archive/refs/heads/main.zip
RUN tar -xf pipeline.zip 

RUN echo "Fetching complete"

ENTRYPOINT ["powershell.exe"]
