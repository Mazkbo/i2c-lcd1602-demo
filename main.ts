I2C_LCD1602.i2cLcdInit(39)
I2C_LCD1602.i2cLcdBacklightOff()
basic.pause(5000)
I2C_LCD1602.i2cLcdBacklightOn()
basic.forever(function on_forever() {
    I2C_LCD1602.i2cLcdShowString("Bonjour", 0, 0)
    I2C_LCD1602.i2cLcdShowString("Le monde", 7, 1)
})
