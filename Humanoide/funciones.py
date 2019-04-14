def mover_sevo(n_servo,pos):
    #posicion la reciviremos en un rango de 0 a 4096
    driver.set_pwm(n_servo, 0, pos)
    return
