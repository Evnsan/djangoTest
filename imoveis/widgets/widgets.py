from django.forms.widgets import CheckboxSelectMultiple


class BootstrapedCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = 'imoveis/forms/widgets/multiple_input.html'
    option_template_name = 'imoveis/forms/widgets/input_option.html'
