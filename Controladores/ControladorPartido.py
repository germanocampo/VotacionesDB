from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre_partido = infoPartido["nombre_partido"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)

    def getCandidatos(self, idCandidato):
        return self.repositorioCandidato.getListadoCandidatosEnPartido(idCandidato)

    def getPromedioGeneral(self,idPartido):
        elPartido = self.repositorioPartido.findById(idPartido)
        elPartido["candidato"]=self.repositorioCandidato.getListadoCandidatosEnPartido(idPartido)
        suma=0
        contador=0
        i=0
        for candidatoActual in elPartido["candidato"]:
            listadoResultados=self.repositorioResultado.getListadoResultadosPorCandidato(candidatoActual["_id"])
            elPartido["candidato"][i]["resultados"]=listadoResultados
            i+=1
            for resultadoActual in listadoResultados:
                suma += resultadoActual["total_votos"]
                contador+=1
        promedio=suma/contador
        elPartido["promedio_votos"]=promedio
        return elPartido