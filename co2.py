# -*- coding:utf-8 -*-
import co2meter as co2

def get_co2():
  return(co2.CO2monitor().read_data())

if __name__ == "__main__":
  print(get_co2())