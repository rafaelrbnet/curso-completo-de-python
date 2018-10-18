from SshOps import SshOps


class DockerOps:

    def __init__(self):
        pass

    def create_container(self, id, image):
        command = "docker run -d -ti --name %s %s" % ("%s_%s" % (image, id), 'debian')
        ssh = SshOps()
        res = ssh.run_command(command)
        if res['status'] == 1:
            print(res['message'])
        else:
            command = 'docker exec %s uname -a %s' % (id, image)
            res = ssh.run_command(command)
