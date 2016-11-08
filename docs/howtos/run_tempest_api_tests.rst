Clone the Subject Code
======================

#. `git clone -b liberty git@github.com:F5Networks/f5-openstack-lbaasv2-driver.git`
    ONCE we get merged forward it won't be "liberty"
#. docker run -it -v `pwd`:/root/devenv -v /var/run/docker.sock:/var/run/docker.sock -v `pwd`/.ssh/id_rsa_bldrgit:/root/ssh_keys/id_rsa_bldrgit -v `pwd`/.ssh/id_rsa_testlab:/root/ssh_keys/id_rsa_testlab  docker-registry.pdbld.f5net.com/f5-openstack-test/devenvironments/base bash
