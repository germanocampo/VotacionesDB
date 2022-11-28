from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Candidato import Candidato
from bson import ObjectId
class RepositorioCandidato(InterfaceRepositorio[Candidato]):
    def getListadoCandidatosEnPartido(self, id_candidato):
        theQuery = {"id_partido.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
