import humanize as h
from datetime import datetime, timedelta

# Tamanho de arquivos
val = 300
print(val)
print(h.naturalsize(val))


val = 3_000_000
print(val)
print(h.naturalsize(val))



# Datas e tempo
print(h.naturalday(datetime.now()))
print(h.naturalday(datetime.now() - timedelta(365)))
print(h.naturalday(datetime.now() + timedelta(1)))

print(h.naturaldate(datetime.now()))
print(h.naturaldate(datetime.now() - timedelta(365)))
print(h.naturaldate(datetime.now() + timedelta(1)))
print(h.naturaldelta(timedelta(30)))

# distância
print(h.naturaldelta(timedelta(31)))

print(h.precisedelta(timedelta(31)))

print(h.precisedelta(
  timedelta(hours=10, seconds=-35),
  minimum_unit='hours'))

print(h.precisedelta(
  timedelta(10, hours=10, seconds=10),
  minimum_unit='seconds'))

# Setando para Brasil
h.activate('pt_BR')

val = 3_000_000
print(val)
print(h.naturalsize(val))



# Datas e tempo
print(h.naturalday(datetime.now()))
print(h.naturalday(datetime.now() - timedelta(365)))
print(h.naturalday(datetime.now() + timedelta(1)))

print(h.naturaldate(datetime.now()))
print(h.naturaldate(datetime.now() - timedelta(365)))
print(h.naturaldate(datetime.now() + timedelta(1)))
print(h.naturaldelta(timedelta(30)))

# distância
print(h.naturaldelta(timedelta(31)))

print(h.precisedelta(timedelta(31)))

print(h.precisedelta(
  timedelta(hours=10, seconds=-35),
  minimum_unit='hours'))

print(h.precisedelta(
  timedelta(10, hours=10, seconds=10),
  minimum_unit='seconds'))

print(h.ordinal(1))

# Desativar o humanização para Brasileiro
# h.deactivate()


# Numeros
print(h.fractional(.5))
print(h.fractional(3.663))

print(h.scientific(100000000000000000654654894656565))

print(h.metric(19, 'F'))

print(h.ordinal(1))
print(h.ordinal(56, gender="female"))


print(h.intcomma(1.10))
print(h.intcomma(5.67))


print(h.intword(2_000))
print(h.intword(2_000_000))


# List
print(h.natural_list([1, 2, 3]))

