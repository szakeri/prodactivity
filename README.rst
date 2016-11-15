Components
----------

TestRunner
~~~~~~~~~~
A container designed to run and record a suite of tests with
the following properties:

  Requirements:
    (#). The test infrastructure MUST be sufficient for ALL tests in the suite.
    (#). The tests are specified by a (routable) git repository and commit
    (#). The TestRunner MUST have a route and permissions for a registry, that
it can be published-to/pulled-from.

How it works:

  As a docker-style specification the TestRunner goes through a standard 
lifecycle.

1 generic_template_of_dockerfile: A file with common Dockerfile logic.
               |
               V
2 Dockerfile_specific_to_testrun: Includes infraparameters, subjectcode, etc.
               |
               V
3 Docker_image_to_be_run: running this, produces a container that...
               |
               V
4 Docker_TestRunner_container: ...runs the tests, and records results.
               |
               V
5 Docker_test_RESULTS_image: committed from container, published to registry


  The TestRunner begins life in infrastructure that has been set up to run a
particular set of tests.   The insfrastructure (test environment from the
perspective of the runner) MUST be sufficient to run all the tests that the 
runner orders.  The parameters of that infrastructure are recorded in the
image.

 The specific test infrastructure and subjectcode a given TestRunner interracts
with ccan be read from the unique tag that is used to publish the TestRunner.
For example:


 The TestRunner is anchored to that infrastructure via a set of environment
variables that are passed into its Dockerfile during the `docker build` step of
its lifecycle.    So, each TestRunner has a set of environment variables that
reference *specific* test infrastructure.   To examine the set of environment
variables specified by given a TestRunner  

Functions:

1.  Provide a reproducible lightweight development sandbox.
2.  Provide tools for containerized, automatable testing, including:

    1. TestRunner deginitions defining docker images via Dockerfiles, building, and pushing docker images to be used
by automated test infrastruct


