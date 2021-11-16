"""
    sff8024.py

    Implementation of SFF-8024 Rev 4.8a
"""

from ..xcvr_codes import XcvrCodes

class Sff8024(XcvrCodes):
    XCVR_IDENTIFIERS = {
        0: 'Unknown or unspecified',
        1: 'GBIC',
        2: 'Module/connector soldered to motherboard',
        3: 'SFP/SFP+/SFP28',
        4: '300 pin XBI',
        5: 'XENPAK',
        6: 'XFP',
        7: 'XFF',
        8: 'XFP-E',
        9: 'XPAK',
        10: 'X2',
        11: 'DWDM-SFP/SFP+',
        12: 'QSFP',
        13: 'QSFP+ or later with SFF-8636 or SFF-8436',
        14: 'CXP or later',
        15: 'Shielded Mini Multilane HD 4X',
        16: 'Shielded Mini Multilane HD 8X',
        17: 'QSFP28 or later',
        18: 'CXP2 (aka CXP28) or later',
        19: 'CDFP (Style 1/Style2)',
        20: 'Shielded Mini Multilane HD 4X Fanout Cable',
        21: 'Shielded Mini Multilane HD 8X Fanout Cable',
        22: 'CDFP (Style 3)',
        23: 'microQSFP',
        24: 'QSFP-DD Double Density 8X Pluggable Transceiver',
        25: 'OSFP 8X Pluggable Transceiver',
        26: 'SFP-DD Double Density 2X Pluggable Transceiver',
        27: 'DSFP Dual Small Form Factor Pluggable Transceiver',
        28: 'x4 MiniLink/OcuLink',
        29: 'x8 MiniLink',
        30: 'QSFP+ or later with CMIS'
    }

    XCVR_IDENTIFIER_ABBRV = {
        0: 'Unknown',
        1: 'GBIC',
        2: 'Soldered',
        3: 'SFP',
        4: 'XBI300',
        5: 'XENPAK',
        6: 'XFP',
        7: 'XFF',
        8: 'XFP-E',
        9: 'XPAK',
        10: 'X2',
        11: 'DWDM-SFP',
        12: 'QSFP',
        13: 'QSFP+',
        14: 'CXP',
        15: 'HD4X',
        16: 'HD8X',
        17: 'QSFP28',
        18: 'CXP2',
        19: 'CDFP-1/2',
        20: 'HD4X-Fanout',
        21: 'HD8X-Fanout',
        22: 'CDFP-3',
        23: 'MicroQSFP',
        24: 'QSFP-DD',
        25: 'OSFP-8X',
        26: 'SFP-DD',
        27: 'DSFP',
        28: 'Link-x4',
        29: 'Link-x8',
        30: 'QSFP+'
    }

    CONNECTORS = {
        0: 'Unknown or unspecified',
        1: 'SC',
        2: 'FC Style 1 copper connector',
        3: 'FC Style 2 copper connector',
        4: 'BNC/TNC',
        5: 'FC coax headers',
        6: 'Fiberjack',
        7: 'LC',
        8: 'MT-RJ',
        9: 'MU',
        10: 'SG',
        11: 'Optical Pigtail',
        12: 'MPO 1x12',
        13: 'MPO 2x16',
        32: 'HSSDC II',
        33: 'Copper pigtail',
        34: 'RJ45',
        35: 'No separable connector',
        36: 'MXC 2x16',
        37: 'CS optical connector',
        38: 'SN optical connector',
        39: 'MPO 2x12',
        40: 'MPO 1x16'
    }

    ENCODINGS = {
        0: "Unspecified",
        1: "8B/10B",
        2: "4B/5B",
        3: "NRZ",
        # 4-6 differ between 8472 and 8436/8636
        7: "256B/257B (transcoded FEC-enabled data)",
        8: "PAM4"
    }

    EXT_SPEC_COMPLIANCE = {
        0: 'Unspecified',
        1: '100G AOC (Active Optical Cable) or 25GAUI C2M AOC',
        2: '100GBASE-SR4 or 25GBASE-SR',
        3: '100GBASE-LR4 or 25GBASE-LR',
        4: '100GBASE-ER4 or 25GBASE-ER',
        5: '100GBASE-SR10',
        6: '100G CWDM4',
        7: '100G PSM4 Parallel SMF',
        8: '100G ACC (Active Copper Cable) or 25GAUI C2M ACC',
        9: 'Obsolete (assigned before 100G CWDM4 MSA required FEC)',
        11: '100GBASE-CR4, 25GBASE-CR CA-25G-L or 50GBASE-CR2 with RS',
        12: '25GBASE-CR CA-25G-S or 50GBASE-CR2 with BASE-R',
        13: '25GBASE-CR CA-25G-N or 50GBASE-CR2 with no FEC',
        14: '10 Mb/s Single Pair Ethernet',
        16: '40GBASE-ER4',
        17: '4 x 10GBASE-SR',
        18: '40G PSM4 Parallel SMF',
        19: 'G959.1 profile P1I1-2D1 (10709 MBd, 2km, 1310 nm SM)',
        20: 'G959.1 profile P1S1-2D2 (10709 MBd, 40km, 1550 nm SM)',
        21: 'G959.1 profile P1L1-2D2 (10709 MBd, 80km, 1550 nm SM)',
        22: '10GBASE-T with SFI electrical interface',
        23: '100G CLR4',
        24: '100G AOC or 25GAUI C2M AOC',
        25: '100G ACC or 25GAUI C2M ACC',
        26: '100GE-DWDM2',
        27: '100G 1550nm WDM',
        28: '10GBASE-T Short Reach',
        29: '5GBASE-T',
        30: '2.5GBASE-T',
        31: '40G SWDM4',
        32: '100G SWDM4',
        33: '100G PAM4 BiDi',
        34: '4WDM-10 MSA',
        35: '4WDM-20 MSA',
        36: '4WDM-40 MSA',
        37: '100GBASE-DR',
        38: '100G-FR or 100GBASE-FR1',
        39: '100G-LR or 100GBASE-LR1',
        40: '100G-SR1',
        41: '100GBASE-SR1, 200GBASE-SR2 or 400GBASE-SR4',
        42: '100GBASE-FR1',
        43: '100GBASE-LR1',
        48: 'Active Copper Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 10-6 or below',
        49: 'Active Optical Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 10-6 or below',
        50: 'Active Copper Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 2.6x10-4 for ACC, 10-5 for AUI, or below',
        51: 'Active Optical Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 2.6x10-4 for AOC, 10-5 for AUI, or below',
        63: '100GBASE-CR1, 200GBASE-CR2 or 400GBASE-CR4',
        64: '50GBASE-CR, 100GBASE-CR2, or 200GBASE-CR4',
        65: '50GBASE-SR, 100GBASE-SR2, or 200GBASE-SR4',
        66: '50GBASE-FR or 200GBASE-DR4',
        67: '200GBASE-FR4',
        68: '200G 1550 nm PSM4',
        69: '50GBASE-LR',
        70: '200GBASE-LR4',
        71: '400GBASE-DR4, 100GAUI-1 C2M',
        72: '400GBASE-FR4',
        73: '400GBASE-LR4-6',
        127: '256GFC-SW4',
        128: 'Capable of 64GFC',
        129: 'Capable of 128GFC'
    }


    MODULE_MEDIA_TYPE = {
        0: 'Undefined',
        1: 'Multimode Fiber (MMF)',
        2: 'Single Mode Fiber (SMF)',
        3: 'Passive Copper Cable',
        4: 'Active Cable Assembly',
        5: 'BASE-T'
    }

    HOST_ELECTRICAL_INTERFACE = {
        0: 'Undefined',
        1: '1000BASE -CX(Clause 39)',
        2: 'XAUI(Clause 47)',
        3: 'XFI (SFF INF-8071i)',
        4: 'SFI (SFF-8431)',
        5: '25GAUI C2M (Annex 109B)',
        6: 'XLAUI C2M (Annex 83B)',
        7: 'XLPPI (Annex 86A)',
        8: 'LAUI-2 C2M (Annex 135C)',
        9: '50GAUI-2 C2M (Annex 135E)',
        10: '50GAUI-1 C2M (Annex 135G)',
        11: 'CAUI-4 C2M (Annex 83E)',
        12: '100GAUI-4 C2M (Annex 135E)',
        13: '100GAUI-2 C2M (Annex 135G)',
        14: '200GAUI-8 C2M (Annex 120C)',
        15: '200GAUI-4 C2M (Annex 120E)',
        16: '400GAUI-16 C2M (Annex 120C)',
        17: '400GAUI-8 C2M (Annex 120E)',
        19: '10GBASE-CX4 (Clause 54)',
        20: '25GBASE-CR CA-L (Clause 110)',
        21: '25GBASE-CR CA-S (Clause 110)',
        22: '25GBASE-CR CA-N (Clause 110)',
        23: '40GBASE-CR4 (Clause 85)',
        24: '50GBASE-CR (Clause 126)',
        25: '100GBASE-CR10 (Clause 85)',
        26: '100GBASE-CR4 (Clause 92)',
        27: '100GBASE-CR2 (Clause 136)',
        28: '200GBASE-CR4 (Clause 136)',
        29: '400G CR8',
        30: '1000BASE-T (Clause 40)',
        31: '2.5GBASE-T (Clause 126)',
        32: '5GBASE-T (Clause 126)',
        33: '10GBASE-T (Clause 55)',
        34: '25GBASE-T (Clause 113)',
        35: '40GBASE-T (Clause 113)',
        36: '50GBASE-T (Placeholder)',
        37: '8GFC (FC-PI-4)',
        38: '10GFC (10GFC)',
        39: '16GFC (FC-PI-5)',
        40: '32GFC (FC-PI-6)',
        41: '64GFC (FC-PI-7)',
        42: '128GFC (FC-PI-6P)',
        43: '256GFC (FC-PI-7P)',
        44: 'IB SDR (Arch.Spec.Vol.2)',
        45: 'IB DDR (Arch.Spec.Vol.2)',
        46: 'IB QDR (Arch.Spec.Vol.2)',
        47: 'IB FDR (Arch.Spec.Vol.2)',
        48: 'IB EDR (Arch.Spec.Vol.2)',
        49: 'IB HDR (Arch.Spec.Vol.2)',
        50: 'IB NDR',
        51: 'E.96 (CPRI Specification V7.0)',
        52: 'E.99 (CPRI Specification V7.0)',
        53: 'E.119 (CPRI Specification V7.0)',
        54: 'E.238 (CPRI Specification V7.0)',
        55: 'OTL3.4 (ITU-T G.709/Y.1331 G.Sup58)',
        56: 'OTL4.10 (ITU-T G.709/Y.1331 G.Sup58)',
        57: 'OTL4.4 (ITU-T G.709/Y.1331 G.Sup58)',
        58: 'OTLC.4 (ITU-T G.709.1/Y.1331 G.Sup58)',
        59: 'FOIC1.4 (ITU-T G.709.1/Y.1331 G.Sup58)',
        60: 'FOIC1.2 (ITU-T G.709.1/Y.1331 G.Sup58)',
        61: 'FOIC2.8 (ITU-T G.709.1/Y.1331 G.Sup58)',
        62: 'FOIC2.4 (ITU-T G.709.1/Y.1331 G.Sup58)',
        63: 'FOIC4.16 (ITU-T G.709.1 G.Sup58)',
        64: 'FOIC4.8 (ITU-T G.709.1 G.Sup58)'
    }

    NM_850_MEDIA_INTERFACE = {
        0: 'Undefined',
        1: '10GBASE-SW (Clause 52)',
        2: '10GBASE-SR (Clause 52)',
        3: '25GBASE-SR (Clause 112)',
        4: '40GBASE-SR4 (Clause 86)',
        5: '40GE SWDM4 MSA Spec',
        6: '40GE BiDi',
        7: '50GBASE-SR (Clause 138)',
        8: '100GBASE-SR10 (Clause 86)',
        9: '100GBASE-SR4 (Clause 95)',
        10: '100GE SWDM4 MSA Spec',
        11: '100GE BiDi',
        12: '100GBASE-SR2 (Clause 138)',
        13: '100G-SR (Placeholder)',
        14: '200GBASE-SR4 (Clause 138)',
        15: '400GBASE-SR16 (Clause 123)',
        16: '400GBASE-SR8 (Clause 138)',
        17: '400G-SR4 (Placeholder)',
        18: '800G-SR8 (Placeholder)',
        26: '400GBASE-SR4.2 (Clause 150) (400GE BiDi)',
        19: '8GFC-MM (FC-PI-4)',
        20: '10GFC-MM (10GFC)',
        21: '16GFC-MM (FC-PI-5)',
        22: '32GFC-MM (FC-PI-6)',
        23: '64GFC-MM (FC-PI 7)',
        24: '128GFC-MM4 (FC-PI-6P)',
        25: '256GFC-MM4 (FC-PI-7P)'
    }

    SM_MEDIA_INTERFACE = {
        0: 'Undefined',
        1: '10GBASE-LW (Cl 52)',
        2: '10GBASE-EW (Cl 52)',
        3: '10G-ZW',
        4: '10GBASE-LR (Cl 52)',
        5: '10GBASE-ER (Cl 52)',
        6: '10G-ZR',
        7: '25GBASE-LR (Cl 114)',
        8: '25GBASE-ER (Cl 114)',
        9: '40GBASE-LR4 (Cl 87)',
        10: '40GBASE-FR (Cl 89)',
        11: '50GBASE-FR (Cl 139)',
        12: '50GBASE-LR (Cl 139)',
        13: '100GBASE-LR4 (Cl 88)',
        14: '100GBASE-ER4 (Cl 88)',
        15: '100G PSM4 MSA Spec',
        16: '100G CWDM4 MSA Spec',
        17: '100G 4WDM-10 MSA Spec',
        18: '100G 4WDM-20 MSA Spec',
        19: '100G 4WDM-40 MSA Spec',
        20: '100GBASE-DR (Cl 140)',
        21: '100G-FR/100GBASE-FR1 (Cl 140)',
        22: '100G-LR/100GBASE-LR1 (Cl 140)',
        23: '200GBASE-DR4 (Cl 121)',
        24: '200GBASE-FR4 (Cl 122)',
        25: '200GBASE-LR4 (Cl 122)',
        26: '400GBASE-FR8 (Cl 122)',
        27: '400GBASE-LR8 (Cl 122)',
        28: '400GBASE-DR4 (Cl 124)',
        29: '400G-FR4/400GBASE-FR4 (Cl 151)',
        30: '400G-LR4-10',
        31: '8GFC-SM (FC-PI-4)',
        32: '10GFC-SM (10GFC)',
        33: '16GFC-SM (FC-PI-5)',
        34: '32GFC-SM (FC-PI-6)',
        35: '64GFC-SM (FC-PI-7)',
        36: '128GFC-PSM4 (FC-PI-6P)',
        37: '256GFC-PSM4 (FC-PI-7P)',
        38: '128GFC-CWDM4 (FC-PI-6P)',
        39: '256GFC-CWDM4 (FC-PI-7P)',
        44: '4I1-9D1F (G.959.1)',
        45: '4L1-9C1F (G.959.1)',
        46: '4L1-9D1F (G.959.1)',
        47: 'C4S1-9D1F (G.695)',
        48: 'C4S1-4D1F (G.695)',
        49: '4I1-4D1F (G.959.1)',
        50: '8R1-4D1F (G.959.1)',
        51: '8I1-4D1F (G.959.1)',
        56: '10G-SR',
        57: '10G-LR',
        58: '25G-SR',
        59: '25G-LR',
        60: '10G-LR-BiDi',
        61: '25G-LR-BiDi',
        62: '400ZR, DWDM, amplified',
        63: '400ZR, Single Wavelength, Unamplified',
        70: 'ZR400-OFEC-16QAM',
        71: 'ZR300-OFEC-8QAM',
        72: 'ZR200-OFEC-QPSK',
        73: 'ZR100-OFEC-QPSK'
    }

    PASSIVE_COPPER_MEDIA_INTERFACE = {
        0: 'Undefined',
        1: 'Copper cable',
        2: 'Passive Loopback module'
    }

    ACTIVE_CABLE_MEDIA_INTERFACE = {
        0: 'Undefined',
        1: 'Active Cable assembly with BER < 10^-12',
        2: 'Active Cable assembly with BER < 5x10^-5',
        3: 'Active Cable assembly with BER < 2.6x10^-4',
        4: 'Active Cable assembly with BER < 10^-6',
        191: 'Active Loopback module'
    }

    BASE_T_MEDIA_INTERFACE = {
        0: 'Undefined',
        1: '1000BASE-T (Clause 40)',
        2: '2.5GBASE-T (Clause 126)',
        3: '5GBASE-T (Clause 126)',
        4: '10GBASE-T (Clause 55)'
    }

    # TODO: Add other codes
