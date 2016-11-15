Clone the Subject Code
======================

#. cd ~
#. Add ssh key "id_rsa_testlab" to ~/.ssh
#. Add ssh key "id_rsa_bldrgit" to ~/.ssh
#. `git clone -b DEVELOPMENT git@github.com:F5Networks/SUBJECTCODE.git`
    NOTE: DEVELOPMENT=liberty ;; SUBJECTCODE=f5-openstack-lbaasv2-driver
#. pip install git+https://github.com/zancas/prodactivity.git
#. prodactivity self-publish
#. prodactivity
