import httpx
import respx
from datetime import datetime
from  typing import Literal, TypeAlias, get_args
import humanize

humanize.activate('pt_BR')

URL_COTACAO = 'https://economia.awesomeapi.com.br/json/last/{}'
Moeda: TypeAlias = Literal['EUR', 'USD', 'BTC']
moedas = humanize.natural_list(get_args(Moeda)).replace('and', 'ou')

def cotacao(moeda: Moeda):
  code = f'{moeda}-BRL'
  try:
    response = httpx.get(URL_COTACAO.format(code))
    data = response.json()[code.replace('-', '')]
    isotime = datetime.fromtimestamp(int()) 
    

    return f'Última cotação ({humanize.naturaltime(isotime)}): {humanize.intcomma(float(data['high']))}'
  except KeyError:
    return f'Código de moeda ({moeda}) inválido. Use {moedas}'
  except httpx.InvalidURL:
    return f'Código de moeda inválido. Use {moedas}'
  except httpx.ConnectError:
    return 'Erro de conexão, tente mais tarde'
  except httpx.TimeoutException:
    return 'Erro de conexão, tente mais tarde'

@respx.mock
def test_dolar():
  # Arange
  mocked_response = httpx.Response(200, json={'USDBRL': {'high': 5.8747, 'timestamp': 0}})
  respx.get(URL_COTACAO.format('USD-BRL')).mock(mocked_response)

  # Act
  result = cotacao('USD')

  # Assert
  assert result == 'Última cotação (há 54 anos): 5,8747'

@respx.mock
def test_moeda_errada():
  # Arange
  mocked_response = httpx.Response(200, json={})
  respx.get(URL_COTACAO.format('MDT-BRL')).mock(mocked_response)

  # Act
  result = cotacao('MDT')

  # Assert
  assert (result == "Código de moeda (MDT) inválido. Use EUR, USD ou BTC")

def test_moeda_errada_erro_URL():
  result = cotacao('\x11')
  assert (result == "Código de moeda inválido. Use EUR, USD ou BTC")

def test_erro_conexao(respx_mock):
  # Arange
  respx_mock.get(URL_COTACAO.format('USD-BRL')).mock(side_effect=httpx.ConnectError)

  # Act
  result = cotacao('USD')

  # Assert
  assert result == 'Erro de conexão, tente mais tarde'

def test_erro_timeout(respx_mock):
  # Arange
  respx_mock.get(URL_COTACAO.format('USD-BRL')).mock(side_effect=httpx.TimeoutException)

  # Act
  result = cotacao('USD')

  # Assert
  assert result == 'Erro de conexão, tente mais tarde'