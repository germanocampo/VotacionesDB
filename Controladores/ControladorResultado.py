from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, infoResultado):
        nuevoResultado = Resultado(infoResultado)
        id_candidato = infoResultado["id_candidato"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.id_candidato = elCandidato
        id_mesa = infoResultado["id_mesa"]
        elMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.id_mesa = elMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.total_votos = infoResultado["total_votos"]
        id_candidato = infoResultado["id_candidato"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultadoActual.id_candidato = elCandidato
        id_mesa = infoResultado["id_mesa"]
        elMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActual.id_mesa = elMesa
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    #Obtener todos los resultados por Candidato
    def listarResultadosPorCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoResultadosPorCandidato(id_candidato)

    def TotalNumeroDeVotosPorCandidato(self, id_candidato):
        return self.repositorioResultado.getTotalNumeroDeVotosPorCandidato(id_candidato)

    def TotalNumberoDeVotosContados(self):
        return self.repositorioResultado.getTotalNumeroDeVotosContados()