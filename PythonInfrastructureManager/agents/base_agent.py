__author__ = 'hiranya'

class BaseAgent:
    """
    BaseAgent class defines the interface that must be implemented by
    each and every cloud agent implementation. This interface defines
    the basic operations such as run_instances and terminate_instances,
    which must be supported by every agent. The InfrastructureManager
    assumes that all agent implementations are based on this interface
    and uses that knowledge to interact with different cloud platforms.
    """

    # Basic operations supported by agents
    OPERATION_RUN = 'run'
    OPERATION_TERMINATE = 'terminate'

    def set_environment_variables(self, parameters, cloud_num):
        """
        Set any cloud platform specific environment variables
        in the current process.

        Arguments:
            - parameters    A dictionary of parameters that may include
                            parameters that should not be actually set in
                            in the current process as environment variables.
                            Agent implementations may decide which subset of
                            parameters should be set as environment variables.
            - cloud_num     A string identifier
        """
        pass

    def configure_instance_security(self, parameters):
        """
        Configure and setup security features for the VMs spawned via this
        agent. This method is called whenever InfrastructureManager is about
        start a set of VMs using this agent. Implementations may configure
        security features such as VM login and firewalls in this method.

         Arguments:
            - parameters    A dictionary of parameters
        """
        raise NotImplementedError

    def describe_instances(self, parameters):
        """
        Query the underlying cloud platform regarding VMs that are already
        up and running.

        Arguments:
            - parameters    A dictionary of parameters

        Returns:
            A tuple of the form (public, private, id) where public is a list
            of private IP addresses, private is a list of private IP addresses
            and id is a list of platform specific VM identifiers.
        """
        raise NotImplementedError

    def run_instances(self, count, parameters, security_configured):
        raise NotImplementedError

    def terminate_instances(self, parameters):
        raise NotImplementedError

    def assert_required_parameters(self, parameters, operation):
        """
        Check whether all the platform specific parameters are present in the
        provided dictionary. If all the parameters required to perform the
        given operation is available this method simply returns. Otherwise
        it throws an AgentConfigurationException.

        Arguments:
            - parameters    A dictionary of parameters
            - operation     Operation for which the parameters should be checked

        Throws:
            - AgentConfigurationException   If a required parameter is absent
        """
        pass

class AgentConfigurationException(Exception):
    def __init__(self,msg):
        Exception.__init__(self, msg)