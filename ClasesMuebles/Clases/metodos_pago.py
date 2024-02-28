class MetodoPago:
    def __init__(self, id, tipo_pago, numero_convenio):
        self.id = id
        self.tipo_pago = tipo_pago
        self.numero_convenio = numero_convenio

    def __str__(self):
        return f"ID del Método de Pago: {self.id}\nTipo de Pago: {self.tipo_pago}\nNúmero de Convenio: {self.numero_convenio}"


