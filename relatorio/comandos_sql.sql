-- Table: alunos
CREATE TABLE IF NOT EXISTS public.alunos
(
    id integer NOT NULL DEFAULT nextval('alunos_id_seq'::regclass),
    matricula bigint NOT NULL,
    nome character varying(80) COLLATE pg_catalog."default" NOT NULL,
    id_disciplina integer,
    CONSTRAINT alunos_pkey PRIMARY KEY (id),
    CONSTRAINT id_disciplina_fk FOREIGN KEY (id_disciplina)
        REFERENCES public.disciplina (id_disc) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

-- Table: Disciplina
CREATE TABLE IF NOT EXISTS public.disciplina
(
    id_disc integer NOT NULL DEFAULT nextval('disciplina_id_disc_seq'::regclass),
    nome character varying(50) COLLATE pg_catalog."default" NOT NULL,
    periodo character varying(7) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT disciplina_pkey PRIMARY KEY (id_disc)
)


-- Table: notas
CREATE TABLE IF NOT EXISTS public.notas
(
    id integer NOT NULL DEFAULT nextval('notas_id_seq'::regclass),
    aluno bigint NOT NULL,
    disciplina integer NOT NULL,
    sm1 double precision NOT NULL,
    sm2 double precision NOT NULL,
    av double precision NOT NULL,
    avs double precision NOT NULL,
    nf double precision NOT NULL,
    aprovado "char" NOT NULL,
    CONSTRAINT notas_pkey PRIMARY KEY (id)
)