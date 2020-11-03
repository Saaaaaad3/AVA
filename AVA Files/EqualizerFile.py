from equalizer_bar import EqualizerBar

equalizer = Equalizer(20,30)
equalizer.setRange(0,100)

equalizer.setDecay(0,100)


equalizer = EqualizerBar(10,  ["#2d004b", "#542788", "#8073ac", "#b2abd2", "#d8daeb", "#f7f7f7", "#fee0b6", "#fdb863", "#e08214", "#b35806", "#7f3b08"])

equalizer.setBarPadding(20)
equalizer.setBackgroundColor('#ffffff00')