from django import forms
from .models import InternatDocuments


class InternatForm(forms.ModelForm):
        class Meta:
            model = InternatDocuments
            fields = '__all__'

            widgets = {
                    'first_name': forms.TextInput(attrs={'class': 'form-control', 'title':"Your name"}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                    # 'category': forms.ChoiceField(),
                    # 'oblast': forms.ChoiceField(),
                    # 'gender': forms.ChoiceField(),
                    'zayavlenye': forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_svid_rozh':forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_vkl_roj_IIN':forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_udos_lich': forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_udos_lich_rod': forms.FileInput(attrs={'class': 'form-control'}),
                    'adress_reg_vseh': forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_prikaz_rab': forms.FileInput(attrs={'class': 'form-control'}),
                    'sprv_akima_or_egov': forms.FileInput(attrs={'class': 'form-control'}),
                    'sprv_rab_zrpl_or_mest_ispol_org': forms.FileInput(attrs={'class': 'form-control'}),
                    'inform_gnpf': forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_svd_rozh_mnodet': forms.FileInput(attrs={'class': 'form-control'}),
                    'sprv_invd': forms.FileInput(attrs={'class': 'form-control'}),
                    'sprv_asp': forms.FileInput(attrs={'class': 'form-control'}),
                    'sprv_neblag_semya': forms.FileInput(attrs={'class': 'form-control'}),
                    'copy_doc_nepol_semya': forms.FileInput(attrs={'class': 'form-control'}),


            }
