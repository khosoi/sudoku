from django import forms
 
class sudokuForm(forms.Form):
    x11 = forms.CharField(label='x11')
    x12 = forms.IntegerField(label='x12')
    x13 = forms.DecimalField(label='x13')
    x14 = forms.DecimalField(label='x14')
    x15 = forms.DecimalField(label='x15')
    x16 = forms.DecimalField(label='x16')
    x17 = forms.DecimalField(label='x17')
    x18 = forms.DecimalField(label='x18')
    x19 = forms.DecimalField(label='x19')

    x21 = forms.DecimalField(label='x21')
    x22 = forms.DecimalField(label='x22')
    x23 = forms.DecimalField(label='x23')
    x24 = forms.DecimalField(label='x24')
    x25 = forms.DecimalField(label='x25')
    x26 = forms.DecimalField(label='x26')
    x27 = forms.DecimalField(label='x27')
    x28 = forms.DecimalField(label='x28')
    x29 = forms.DecimalField(label='x29')

    x31 = forms.DecimalField(label='x31')
    x32 = forms.DecimalField(label='x32')
    x33 = forms.DecimalField(label='x33')
    x34 = forms.DecimalField(label='x34')
    x35 = forms.DecimalField(label='x35')
    x36 = forms.DecimalField(label='x36')
    x37 = forms.DecimalField(label='x37')
    x38 = forms.DecimalField(label='x38')
    x39 = forms.DecimalField(label='x39')

    x41 = forms.DecimalField(label='x41')
    x42 = forms.DecimalField(label='x42')
    x43 = forms.DecimalField(label='x43')
    x44 = forms.DecimalField(label='x44')
    x45 = forms.DecimalField(label='x45')
    x46 = forms.DecimalField(label='x46')
    x47 = forms.DecimalField(label='x47')
    x48 = forms.DecimalField(label='x48')
    x49 = forms.DecimalField(label='x49')

    x51 = forms.DecimalField(label='x51')
    x52 = forms.DecimalField(label='x52')
    x53 = forms.DecimalField(label='x53')
    x54 = forms.DecimalField(label='x54')
    x55 = forms.DecimalField(label='x55')
    x56 = forms.DecimalField(label='x56')
    x57 = forms.DecimalField(label='x57')
    x58 = forms.DecimalField(label='x58')
    x59 = forms.DecimalField(label='x59')

    x61 = forms.DecimalField(label='x61')
    x62 = forms.DecimalField(label='x62')
    x63 = forms.DecimalField(label='x63')
    x64 = forms.DecimalField(label='x64')
    x65 = forms.DecimalField(label='x65')
    x66 = forms.DecimalField(label='x66')
    x67 = forms.DecimalField(label='x67')
    x68 = forms.DecimalField(label='x68')
    x69 = forms.DecimalField(label='x69')

    x71 = forms.DecimalField(label='x71')
    x72 = forms.DecimalField(label='x72')
    x73 = forms.DecimalField(label='x73')
    x74 = forms.DecimalField(label='x74')
    x75 = forms.DecimalField(label='x75')
    x76 = forms.DecimalField(label='x76')
    x77 = forms.DecimalField(label='x77')
    x78 = forms.DecimalField(label='x78')
    x79 = forms.DecimalField(label='x79')
    
    x81 = forms.DecimalField(label='x81')
    x82 = forms.DecimalField(label='x82')
    x83 = forms.DecimalField(label='x83')
    x84 = forms.DecimalField(label='x84')
    x85 = forms.DecimalField(label='x85')
    x86 = forms.DecimalField(label='x86')
    x87 = forms.DecimalField(label='x87')
    x88 = forms.DecimalField(label='x88')
    x89 = forms.DecimalField(label='x89')

    x91 = forms.DecimalField(label='x91')
    x92 = forms.DecimalField(label='x92')
    x93 = forms.DecimalField(label='x93')
    x94 = forms.DecimalField(label='x94')
    x95 = forms.DecimalField(label='x95')
    x96 = forms.DecimalField(label='x96')
    x97 = forms.DecimalField(label='x97')
    x98 = forms.DecimalField(label='x98')
    x99 = forms.DecimalField(label='x99')

#    def __init__(self, *args, **kwargs):
#        super(sudokuForm, self).__init__(*args, **kwargs)
#        for i in range(1,10):
#            self.fields['%s_field' % i] = forms.DecimalField(max_length=1, label=str(i))
