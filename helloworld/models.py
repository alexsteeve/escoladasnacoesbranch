from django.db import models


class TipoCurso(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )


class MesdoAno(models.Model):

    numeroMes = models.IntegerField(
        null=False,
        blank=False
    )

    nomeMes = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    def __str__(self):
        return self.nomeMes

class Escolaridade(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    def __str__(self):
        return self.nome

    objetos = models.Manager()


class Estudante(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    matricula = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    celular = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    batismo = models.BooleanField(
        null=False,
        blank=False
    )

    profissao = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default='Não informado'
    )

    diaAniversario = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    # mesAniversario = models.IntegerField(
    mesAniversario = models.ForeignKey(MesdoAno, on_delete=models.CASCADE)

    #    escolaridade = models.IntegerField(
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    objetos = models.Manager()


class Curso(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    tipoCurso = models.ForeignKey(TipoCurso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    objetos = models.Manager()

class Materia(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    livro1 = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    livro2 = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    objetos = models.Manager()

class CursoPeriodo(models.Model):

    ano = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    semestre = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    local = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    diaSemana = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        default='Domingo'
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    matriculasAbertas = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    def __str__(self):
        return str(self.ano) + "/" + str(self.semestre) + " "+ self.curso.nome

    objetos = models.Manager()


class CursoPeriodoEstudante(models.Model):

    aprovacao = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    presencas = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    financeiro = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    provas = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    trabalhos = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    pagamento = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )

    cursoPeriodo = models.ForeignKey(CursoPeriodo, on_delete=models.CASCADE)

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)

    objetos = models.Manager()


class CursoPeriodoEstudanteFinanceiro(models.Model):

    pagamentos = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        default=False
    )

    cursoPeriodo = models.ForeignKey(CursoPeriodo, on_delete=models.CASCADE)

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)

    objetos = models.Manager()