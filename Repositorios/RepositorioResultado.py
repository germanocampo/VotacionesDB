from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoResultadosPorCandidato(self, id_candidato):
        theQuery = {"id_candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getTotalNumeroDeVotosPorCandidato(self, id_candidato):
        query1 = {
            '$match': {
                    'id_candidato.$id': ObjectId(id_candidato)
                }
        }
        query2 = {
            '$group': {
                '_id': 1,
                'totalvotos': {
                    '$sum': '$total_votos'
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def getTotalNumeroDeVotosContados(self):
        query1 = {
            '$group': {
                '_id': 1,
                'totalvotos': {
                    '$sum': '$total_votos'
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

    def getTotalNumeroDeVotosContados(self):
        query1 = {
            '$group': {
                '_id': 1,
                'totalvotos': {
                    '$sum': '$total_votos'
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)