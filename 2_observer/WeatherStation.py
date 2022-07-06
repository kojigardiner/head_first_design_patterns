import random
import time
from abc import ABC, abstractmethod
from ast import Str
from typing import List

import numpy as np


# Observer pattern
class Observer(ABC):
    subject: "Subject"

    @abstractmethod
    def update(self):
        raise NotImplementedError


class Subject(ABC):
    observers: List["Observer"]

    @abstractmethod
    def register_observer(self, observer: "Observer"):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer: "Observer"):
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self):
        raise NotImplementedError


# Display


class Display(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


# WeatherData


class WeatherData(Subject):
    _temp_f: float
    _pressure: float
    _humidity: float

    def __init__(self):
        self.observers = []

    def register_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def remove_observer(self, observer: "Observer"):
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update()

    def set_measurements(self, temp_f: float, pressure: float, humidity: float):
        self._temp_f = temp_f
        self._pressure = pressure
        self._humidity = humidity

        self.measurements_changed()

    def measurements_changed(self):
        self.notify_observers()

    def get_temp(self) -> float:
        return self._temp_f

    def get_pressure(self) -> float:
        return self._pressure

    def get_humidity(self) -> float:
        return self._humidity


# Displays
class CurrentConditionsDisplay(Display, Observer):
    _wd: "WeatherData"
    _temp_f: float
    _pressure: float
    _humidity: float

    def __init__(self, wd: "WeatherData"):
        self._wd = wd
        self._wd.register_observer(self)

    def update(self):
        self._temp_f = self._wd.get_temp()
        self._pressure = self._wd.get_pressure()
        self._humidity = self._wd.get_humidity()

        self.display()

    def display(self):
        print(
            f"Current conditions: {self._temp_f}F degrees, {self._pressure} pressure, and {self._humidity}% humidity"
        )


class StatisticsDisplay(Display, Observer):
    _wd: "WeatherData"
    _temp_f = None
    _pressure = None
    _humidity = None

    def __init__(self, wd: "WeatherData"):
        self._wd = wd
        self._temp_f = np.array([])
        self._pressure = np.array([])
        self._humidity = np.array([])

        self._wd.register_observer(self)

    def update(self):
        self._temp_f = self._wd.get_temp()
        self._pressure = self._wd.get_pressure()
        self._humidity = self._wd.get_humidity()

        self.display()

    def display(self):
        if np.size(self._temp_f) > 0:
            print(
                f"Avg/max/min temperature: {np.average(self._temp_f)}/{np.max(self._temp_f)}/{np.min(self._temp_f)}"
            )


class ForecastDisplay(Display, Observer):
    _wd: "WeatherData"
    _forecasts: List[str]

    def __init__(self, wd: "WeatherData"):
        self._wd = wd
        self._wd.register_observer(self)

        self._forecasts = [
            "Improving weather on the way!",
            "Watch out for cooler, rainy weather",
            "More of the same",
        ]

    def update(self):
        self.display()

    def display(self):
        print(f"Forecast: {random.choice(self._forecasts)}")


# Displays
class HeatIndexDisplay(Display, Observer):
    _wd: "WeatherData"
    _temp_f: float
    _pressure: float
    _humidity: float
    _heat_index: float

    def __init__(self, wd: "WeatherData"):
        self._wd = wd
        self._wd.register_observer(self)

    def update(self):
        self._temp_f = self._wd.get_temp()
        self._pressure = self._wd.get_pressure()
        self._humidity = self._wd.get_humidity()

        T2 = pow(self._temp_f, 2)
        H2 = pow(self._humidity, 2)
        T3 = pow(self._temp_f, 3)
        H3 = pow(self._humidity / 100, 3)

        # Coefficients for the calculations
        C3 = [
            16.923,
            0.185212,
            5.37941,
            -0.100254,
            0.00941695,
            0.00728898,
            0.000345372,
            -0.000814971,
            0.0000102102,
            -0.000038646,
            0.0000291583,
            0.00000142721,
            0.000000197483,
            -0.0000000218429,
            0.000000000843296,
            -0.0000000000481975,
        ]

        # Calculating heat-indexes with 3 different formula
        self._heat_index = (
            C3[0]
            + (C3[1] * self._temp_f)
            + (C3[2] * self._humidity)
            + (C3[3] * self._temp_f * self._humidity)
            + (C3[4] * T2)
            + (C3[5] * H2)
            + (C3[6] * T2 * self._humidity)
            + (C3[7] * self._temp_f * H2)
            + (C3[8] * T2 * H2)
            + (C3[9] * T3)
            + (C3[10] * H3)
            + (C3[11] * T3 * self._humidity)
            + (C3[12] * self._temp_f * H3)
            + (C3[13] * T3 * H2)
            + (C3[14] * T2 * H3)
            + (C3[15] * T3 * H3)
        )

        self.display()

    def display(self):
        print(f"Heat index is {self._heat_index}")


if __name__ == "__main__":
    wd = WeatherData()

    current_conditions_display = CurrentConditionsDisplay(wd)
    statistics_display = StatisticsDisplay(wd)
    forecast_display = ForecastDisplay(wd)
    heat_index_display = HeatIndexDisplay(wd)

    wd.set_measurements(80, 30.4, 65)
    time.sleep(1)
    wd.set_measurements(82, 29.2, 70)
    time.sleep(1)
    wd.set_measurements(78, 29.2, 90)
