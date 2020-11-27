I2C_LCD1602.i2c_lcd_init(39)
I2C_LCD1602.i2c_lcd_backlight_off()
basic.pause(5000)
I2C_LCD1602.i2c_lcd_backlight_on()

def on_forever():
    I2C_LCD1602.i2c_lcd_show_string("Bonjour", 0, 0)
    I2C_LCD1602.i2c_lcd_show_string("Le monde", 7, 1)
basic.forever(on_forever)
