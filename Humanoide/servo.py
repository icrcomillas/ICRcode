def mover_servo(n_servo,pos):
    #posicion la reciviremos en un rango de 0 a 4096
    RANGO_MAXIMO = 4096
    if pos > RANGO_MAXIMO:
        print("no se puede mover ese rango, esta fuera del alcance")
    elif pos< RANGO_MAXIMO:
        driver.set_pwm(n_servo, 0, pos)
    return
