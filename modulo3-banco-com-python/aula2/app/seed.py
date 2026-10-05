from app.database import SessionLocal, Base, engine
from app.models import Departamento, Cargo, Funcionario


def popular_banco():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()   # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])
        db.add_all([
        Funcionario(nome='Gustavo Santos', email='gustavo.santos@empresa.com', telefone='56832710832', salario=4500.00),
        Funcionario(nome='Natha Braga', email='natha.braga@empresa.com', telefone='36936930380', salario=3200.00),
        Funcionario(nome='Ana Laura', email='ana.laura@empresa.com', telefone='34509876567', salario=6800.00),
        Funcionario(nome='Igor Silva', email='igor.silva@empresa.com', telefone='15785409856', salario=2900.00),
    ])

        db.commit()     # confirma tudo no banco de uma vez
        print('Banco preenchido com sucesso')

    except Exception as erro:
        db.rollback()   # desfaz tudo se der erro
        print(f'Erro: {erro}')
    finally:
        db.close()      # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()