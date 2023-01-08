# syntax=docker/dockerfile:1.3
FROM continuumio/miniconda3 as build_image

# copy environment file first to check dependencies
COPY environment.yml .
# run the following command with bash
SHELL ["/bin/bash", "-c"]
# run commands with && to create a single cached layer
RUN conda install mamba -n base -c conda-forge && \
    mamba env create -f environment.yml && \
    mamba install -c conda-forge conda-pack

# conda-pack creates a Python venv; we no longer need conda/mamba
RUN conda-pack -n dev-container -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar

RUN /venv/bin/conda-unpack


FROM debian:buster AS runtime_image

# Copy /venv which contains the venv created based on the conda environment
COPY --from=build_image /venv /venv
