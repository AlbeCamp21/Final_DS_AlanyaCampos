import pytest

# Fixture donde se crea un usuario ficticio, con los atributos nombre, edad y autorizado
@pytest.fixture
def user_fixture():
    class usuario:
        def __init__(self, nombre, edad, autorizado):
            self.nombre = nombre
            self.edad = edad
            self.autorizado = autorizado
    return usuario("Luis", 50, True)

# Fixture que depende de la clase usuario definida en el fixture anterior
# y simula que el cliente esté autenticado
@pytest.fixture
def authenticated_client_fixture():
    class auntenticacion:
        def __init__(self, usuario):
            self.usuario = usuario
        def esta_autenticado(self):
            return self.usuario.autorizado
        def devolver_usuario_info(self):
            return {
                "nombre": self.usuario.nombre,
                "edad": self.usuario.edad
            }
    return autenticacion

# Test para verificar que el cliente autenticado puede acceder a los datos del usuario, va a fallar
@pytest.mark.xfail
def test_usuario_autenticado(user_fixture, authenticated_client_fixture):
    pobar_cliente_autorizado = authenticated_client_fixture(user_fixture)
    assert probar_cliente_autorizado.esta_autenticado() == user_fixture.autorizado

# Test para verificar que cliente autenticado devuleve la informacion del usuario
@pytest.mark.skip
def test_devolver_informacion_usuario(user_fixture, authenticated_client_fixture):
    pobar_cliente_autorizado = authenticated_client_fixture(user_fixture)
    info_usuario = pobar_cliente_autorizado.devolver_usuario_info()
    assert info_usuario["nombre"] == user_fixture.nombre
    assert info_usuario["edad"] == user_fixture.edad
    assert info_usuario["autorizado"] == user_fixture.autorizado