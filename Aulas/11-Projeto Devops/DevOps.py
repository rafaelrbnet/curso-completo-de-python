from MongoOps import MongoOps
from ProvisionOps import ProvisionOps


def start():
    mongo = MongoOps()
    queue = mongo.get_queue()

    print("Existem %s servicos na fila " % queue.count())

    for service in mongo.get_service_to_install():
        print("Instalando servico: ", service["_id"])
        prov = ProvisionOps(service["_id"])
        res = prov.install_service()


if __name__ == "__main__":
    start()
