import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.controls.clear()
        miglia = self._view._txtIn.value

        try:
            nMiglia = float(miglia)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un intero."))
            self._view.update_page()
            return
        nNodi,nArchi,archi = self._model.addEdge(nMiglia)
        self._view._txt_result.controls.append(ft.Text("Graph created!"))
        self._view._txt_result.controls.append(ft.Text(f"Num of nodes: {nNodi}"))
        self._view._txt_result.controls.append(ft.Text(f"Num of edge: {nArchi}"))
        print(archi)
        for a in archi:
            self._view._txt_result.controls.append(ft.Text(f"{a[0].AIRPORT} -> {a[1].AIRPORT} -- AvgDist: {self._model.getAvgDist(a[0],a[1])}"))
        self._view.update_page()
