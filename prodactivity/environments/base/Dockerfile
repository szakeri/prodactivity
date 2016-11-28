FROM ubuntu:16.10

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y\
     docker.io \
     git \
     make \
     python \
     python-pip \
     ssh \
     sudo &&\
    pip install --upgrade pip &&\
    pip install --upgrade git+https://github.com/zancas/prodactivity.git &&\
    pip install --upgrade git+https://bldr-git.int.lineratesystems.com/tools/pytest-symbols.git &&\
    pip install --upgrade git+https://bldr-git.int.lineratesystems.com/tools/pytest-meta.git &&\
    pip install --upgrade git+https://bldr-git.int.lineratesystems.com/tools/pytest-autlog.git &&\
    pip install --upgrade git+https://bldr-git.int.lineratesystems.com/tools/testenv.git &&\
    pip install --upgrade git+https://bldr-git.int.lineratesystems.com/velcro/systest-common.git &&\
    rm -rf /var/lib/apt/lists/*
