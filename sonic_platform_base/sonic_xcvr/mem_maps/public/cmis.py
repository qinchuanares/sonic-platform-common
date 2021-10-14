"""
    cmis.py

    Implementation of XcvrMemMap for CMIS Rev 4.0
"""

from ..xcvr_mem_map import XcvrMemMap
from ...fields.xcvr_field import (
    CodeRegField,
    HexRegField,
    NumberRegField,
    ListRegField,
    RegGroupField,
    StringRegField,
    RegBitField,
)
from ...fields import consts

PAGE_SIZE = 128

def get_addr(page, offset):
    return PAGE_SIZE * page + offset

class CmisMemMap(XcvrMemMap):
    def __init__(self, codes):
        super(CmisMemMap, self).__init__(codes)

        self.ADMIN_INFO = RegGroupField(consts.ADMIN_INFO_FIELD,
            CodeRegField(consts.ID_FIELD, get_addr(0x0, 128), self.codes['sff8024'].XCVR_IDENTIFIERS),
            StringRegField(consts.VENDOR_NAME_FIELD, get_addr(0x0, 129), size=16),
            HexRegField(consts.VENDOR_OUI_FIELD, get_addr(0x0, 145), size=3),
            StringRegField(consts.VENDOR_PART_NO_FIELD, get_addr(0x0, 148), size=16),
            StringRegField(consts.VENDOR_REV_FIELD, get_addr(0x0, 164), size=2),
            StringRegField(consts.VENDOR_SERIAL_NO_FIELD, get_addr(0x0, 166), size=16),
            StringRegField(consts.VENDOR_DATE_FIELD,get_addr(0x0,182), size = 8),
            CodeRegField(consts.CONNECTOR_FIELD, get_addr(0x0, 203), self.codes['sff8024'].CONNECTORS),
            CodeRegField(consts.HOST_ELECTRICAL_INTERFACE, get_addr(0x0, 86), self.codes['sff8024'].HOST_ELECTRICAL_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_TYPE, get_addr(0x0, 85), self.codes['sff8024'].MODULE_MEDIA_TYPE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_850NM, get_addr(0x0, 87), self.codes['sff8024'].NM_850_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_SM, get_addr(0x0, 87), self.codes['sff8024'].SM_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, get_addr(0x0, 87), self.codes['sff8024'].PASSIVE_COPPER_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, get_addr(0x0, 87), self.codes['sff8024'].ACTIVE_CABLE_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_BASE_T, get_addr(0x0, 87), self.codes['sff8024'].BASE_T_MEDIA_INTERFACE),
            NumberRegField(consts.LANE_COUNT, get_addr(0x0, 88), format="B", size=1),
            NumberRegField(consts.HOST_LANE_ASSIGNMENT_OPTION, get_addr(0x0, 89), format="B", size=1),
            NumberRegField(consts.MEDIA_LANE_ASSIGNMENT_OPTION, get_addr(0x1, 176), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_1, get_addr(0x11, 206), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_2, get_addr(0x11, 207), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_3, get_addr(0x11, 208), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_4, get_addr(0x11, 209), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_5, get_addr(0x11, 210), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_6, get_addr(0x11, 211), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_7, get_addr(0x11, 212), format="B", size=1),
            NumberRegField(consts.ACTIVE_APSEL_HOSTLANE_8, get_addr(0x11, 213), format="B", size=1),
            CodeRegField(consts.MEDIA_INTERFACE_TECH, get_addr(0x0, 212), self.codes['cmis_code'].MEDIA_INTERFACE_TECH),
            NumberRegField(consts.HW_MAJOR_REV, get_addr(0x1, 130), size=1),
            NumberRegField(consts.HW_MINOR_REV, get_addr(0x1, 131), size=1),
            NumberRegField(consts.CMIS_REVISION, get_addr(0x0, 1), format="B", size=1),
            NumberRegField(consts.ACTIVE_FW_MAJOR_REV, get_addr(0x0, 39), format="B", size=1),
            NumberRegField(consts.ACTIVE_FW_MINOR_REV, get_addr(0x0, 40), format="B", size=1),
            NumberRegField(consts.INACTIVE_FW_MAJOR_REV, get_addr(0x1, 128), format="B", size=1),
            NumberRegField(consts.INACTIVE_FW_MINOR_REV, get_addr(0x1, 129), format="B", size=1),
            # TODO: add remaining admin fields
        )

        self.TRANS_DOM = RegGroupField(consts.TRANS_DOM_FIELD,
            NumberRegField(consts.CASE_TEMP, get_addr(0x0, 14), format=">h", size=2, scale=256.0),
            NumberRegField(consts.VOLTAGE, get_addr(0x0, 16), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.TX_POW, get_addr(0x11, 154), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.RX_POW, get_addr(0x11, 186), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.TX_BIAS, get_addr(0x11, 170), format=">H", size=2, scale=500.0),
            NumberRegField(consts.GRID_SPACING, get_addr(0x12, 128), size=1, ro=False),
            NumberRegField(consts.LASER_CONFIG_CHANNEL, get_addr(0x12, 136), format=">h", size=2, ro=False),
            NumberRegField(consts.LASER_CURRENT_FREQ, get_addr(0x12, 168), format=">L", size=4),
            NumberRegField(consts.TX_CONFIG_POWER, get_addr(0x12, 200), format=">h", size=2, scale=100.0, ro=False),
            NumberRegField(consts.AUX_MON_TYPE, get_addr(0x1, 145), size=1),
            NumberRegField(consts.AUX1_MON, get_addr(0x0, 18), format=">h", size=2),
            NumberRegField(consts.AUX2_MON, get_addr(0x0, 20), format=">h", size=2),
            NumberRegField(consts.AUX3_MON, get_addr(0x0, 22), format=">h", size=2),
            NumberRegField(consts.CUSTOM_MON, get_addr(0x0, 24), format=">H", size=2),
            )

        self.TRANS_LOOPBACK = RegGroupField(consts.TRANS_LOOPBACK_FIELD,
            NumberRegField(consts.LOOPBACK_CAPABILITY, get_addr(0x13, 128), size=1),
            RegBitField(consts.MEDIA_OUTPUT_LOOPBACK, offset=get_addr(0x13, 180), bitpos=0, ro=False),
            RegBitField(consts.MEDIA_INPUT_LOOPBACK, offset=get_addr(0x13, 181), bitpos=0, ro=False),
            NumberRegField(consts.HOST_OUTPUT_LOOPBACK, get_addr(0x13, 182), size=1, ro=False),
            NumberRegField(consts.HOST_INPUT_LOOPBACK, get_addr(0x13, 183), size=1, ro=False),
        )

        self.TRANS_THRESHOLD = RegGroupField(consts.TRANS_THRESHOLD_FIELD,
            NumberRegField(consts.CASE_TEMP_HIGH_ALARM, get_addr(0x2, 128), format=">h", size=2, scale=256.0),
            NumberRegField(consts.CASE_TEMP_LOW_ALARM, get_addr(0x2, 130), format=">h", size=2, scale=256.0),
            NumberRegField(consts.CASE_TEMP_HIGH_WARN, get_addr(0x2, 132), format=">h", size=2, scale=256.0),
            NumberRegField(consts.CASE_TEMP_LOW_WARN, get_addr(0x2, 134), format=">h", size=2, scale=256.0),
            NumberRegField(consts.VOLTAGE_HIGH_ALARM, get_addr(0x2, 136), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.VOLTAGE_LOW_ALARM, get_addr(0x2, 138), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.VOLTAGE_HIGH_WARN, get_addr(0x2, 140), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.VOLTAGE_LOW_WARN, get_addr(0x2, 142), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.AUX1_HIGH_ALARM, get_addr(0x2, 144), format=">h", size=2),
            NumberRegField(consts.AUX1_LOW_ALARM, get_addr(0x2, 146), format=">h", size=2),
            NumberRegField(consts.AUX1_HIGH_WARN, get_addr(0x2, 148), format=">h", size=2),
            NumberRegField(consts.AUX1_LOW_WARN, get_addr(0x2, 150), format=">h", size=2),
            NumberRegField(consts.AUX2_HIGH_ALARM, get_addr(0x2, 152), format=">h", size=2),
            NumberRegField(consts.AUX2_LOW_ALARM, get_addr(0x2, 154), format=">h", size=2),
            NumberRegField(consts.AUX2_HIGH_WARN, get_addr(0x2, 156), format=">h", size=2),
            NumberRegField(consts.AUX2_LOW_WARN, get_addr(0x2, 158), format=">h", size=2), 
            NumberRegField(consts.AUX3_HIGH_ALARM, get_addr(0x2, 160), format=">h", size=2),
            NumberRegField(consts.AUX3_LOW_ALARM, get_addr(0x2, 162), format=">h", size=2),
            NumberRegField(consts.AUX3_HIGH_WARN, get_addr(0x2, 164), format=">h", size=2),
            NumberRegField(consts.AUX3_LOW_WARN, get_addr(0x2, 166), format=">h", size=2), 
            NumberRegField(consts.TX_POWER_HIGH_ALARM, get_addr(0x2, 176), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.TX_POWER_LOW_ALARM, get_addr(0x2, 178), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.TX_POWER_HIGH_WARN, get_addr(0x2, 180), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.TX_POWER_LOW_WARN, get_addr(0x2, 182), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.TX_BIAS_CURR_HIGH_ALARM, get_addr(0x2, 184), format=">H", size=2, scale=500.0),
            NumberRegField(consts.TX_BIAS_CURR_LOW_ALARM, get_addr(0x2, 186), format=">H", size=2, scale=500.0),
            NumberRegField(consts.TX_BIAS_CURR_HIGH_WARN, get_addr(0x2, 188), format=">H", size=2, scale=500.0),
            NumberRegField(consts.TX_BIAS_CURR_LOW_WARN, get_addr(0x2, 190), format=">H", size=2, scale=500.0),
            NumberRegField(consts.RX_POWER_HIGH_ALARM, get_addr(0x2, 192), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.RX_POWER_LOW_ALARM, get_addr(0x2, 194), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.RX_POWER_HIGH_WARN, get_addr(0x2, 196), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.RX_POWER_LOW_WARN, get_addr(0x2, 198), format=">H", size=2, scale=10000.0),
            NumberRegField(consts.SUPPORT_GRID, get_addr(0x4, 128)),
            NumberRegField(consts.LOW_CHANNEL, get_addr(0x4, 158), format=">h", size=2),
            NumberRegField(consts.HIGH_CHANNEL, get_addr(0x4, 160), format=">h", size=2),
            NumberRegField(consts.MIN_PROG_OUTPUT_POWER, get_addr(0x4, 198), format=">h", size=2, scale = 100.0),
            NumberRegField(consts.MAX_PROG_OUTPUT_POWER, get_addr(0x4, 200), format=">h", size=2, scale = 100.0),
        )

        self.TRANS_MODULE_STATUS = RegGroupField(consts.TRANS_MODULE_STATUS_FIELD,
            NumberRegField(consts.MODULE_STATE, get_addr(0x0, 3), size=1),
            NumberRegField(consts.MODULE_FIRMWARE_FAULT_INFO, get_addr(0x0, 8), size=1),
            NumberRegField(consts.MODULE_FLAG_BYTE1, get_addr(0x0, 9), size=1),
            NumberRegField(consts.MODULE_FLAG_BYTE2, get_addr(0x0, 10), size=1),
            NumberRegField(consts.MODULE_FLAG_BYTE3, get_addr(0x0, 11), size=1),
            NumberRegField(consts.CDB1_STATUS, get_addr(0x0, 37), size=1),
            CodeRegField(consts.MODULE_FAULT_CAUSE, get_addr(0x0, 41), self.codes['cmis_code'].MODULE_FAULT_CAUSE),
        )

        self.TRANS_LANE_STATUS = RegGroupField(consts.TRANS_LANE_STATUS_FIELD,
            NumberRegField(consts.DATAPATH_STATE, get_addr(0x11, 128), format = '>I', size=4),
            NumberRegField(consts.RX_OUTPUT_STATUS, get_addr(0x11, 132), size=1),
            NumberRegField(consts.TX_OUTPUT_STATUS, get_addr(0x11, 133), size=1),
            NumberRegField(consts.TX_FAULT_FLAG, get_addr(0x11, 135), size=1),
            NumberRegField(consts.TX_LOS_FLAG, get_addr(0x11, 136), size=1),
            NumberRegField(consts.TX_CDR_LOL, get_addr(0x11, 137), size=1),
            NumberRegField(consts.TX_POWER_HIGH_ALARM_FLAG, get_addr(0x11, 139), size=1),
            NumberRegField(consts.TX_POWER_LOW_ALARM_FLAG, get_addr(0x11, 140), size=1),
            NumberRegField(consts.TX_POWER_HIGH_WARN_FLAG, get_addr(0x11, 141), size=1),
            NumberRegField(consts.TX_POWER_LOW_WARN_FLAG, get_addr(0x11, 142), size=1),
            NumberRegField(consts.TX_BIAS_HIGH_ALARM_FLAG, get_addr(0x11, 143), size=1),
            NumberRegField(consts.TX_BIAS_LOW_ALARM_FLAG, get_addr(0x11, 144), size=1),
            NumberRegField(consts.TX_BIAS_HIGH_WARN_FLAG, get_addr(0x11, 145), size=1),
            NumberRegField(consts.TX_BIAS_LOW_WARN_FLAG, get_addr(0x11, 146), size=1),
            NumberRegField(consts.RX_LOS_FLAG, get_addr(0x11, 147), size=1),
            NumberRegField(consts.RX_CDR_LOL, get_addr(0x11, 148), size=1),
            NumberRegField(consts.RX_POWER_HIGH_ALARM_FLAG, get_addr(0x11, 149), size=1),
            NumberRegField(consts.RX_POWER_LOW_ALARM_FLAG, get_addr(0x11, 150), size=1),
            NumberRegField(consts.RX_POWER_HIGH_WARN_FLAG, get_addr(0x11, 151), size=1),
            NumberRegField(consts.RX_POWER_LOW_WARN_FLAG, get_addr(0x11, 152), size=1),
            NumberRegField(consts.CONFIG_LANE_STATUS, get_addr(0x11, 202), format=">I", size=4),
            NumberRegField(consts.DPINIT_PENDING, get_addr(0x11, 235), size=1),
            RegBitField(consts.TUNING_IN_PROGRESS, offset=get_addr(0x12, 222), bitpos=1),
            RegBitField(consts.WAVELENGTH_UNLOCKED, offset=get_addr(0x12, 222), bitpos=0),
            NumberRegField(consts.LASER_TUNING_DETAIL, get_addr(0x12, 231), size=1),
        )

        self.TRANS_PM = RegGroupField(consts.TRANS_PM_FIELD,
            NumberRegField(consts.VDM_SUPPORTED_PAGE, get_addr(0x2f, 128), size=1, ro=False),
            NumberRegField(consts.VDM_CONTROL, get_addr(0x2f, 144), size=1, ro=False),
        )

        self.MEDIA_LANE_FEC_PM = RegGroupField(consts.MEDIA_LANE_FEC_PM,
            NumberRegField(consts.RX_BITS_PM, get_addr(0x34, 128), format=">Q", size=8),
            NumberRegField(consts.RX_BITS_SUB_INTERVAL_PM, get_addr(0x34, 136), format=">Q", size=8),
            NumberRegField(consts.RX_CORR_BITS_PM, get_addr(0x34, 144), format=">Q", size=8),
            NumberRegField(consts.RX_MIN_CORR_BITS_SUB_INTERVAL_PM, get_addr(0x34, 152), format=">Q", size=8),
            NumberRegField(consts.RX_MAX_CORR_BITS_SUB_INTERVAL_PM, get_addr(0x34, 160), format=">Q", size=8),
            NumberRegField(consts.RX_FRAMES_PM, get_addr(0x34, 168), format=">I", size=4),
            NumberRegField(consts.RX_FRAMES_SUB_INTERVAL_PM, get_addr(0x34, 172), format=">I", size=4),
            NumberRegField(consts.RX_FRAMES_UNCORR_ERR_PM, get_addr(0x34, 176), format=">I", size=4),
            NumberRegField(consts.RX_MIN_FRAMES_UNCORR_ERR_SUB_INTERVAL_PM, get_addr(0x34, 180), format=">I", size=4),
            NumberRegField(consts.RX_MAX_FRAMES_UNCORR_ERR_SUB_INTERVAL_PM, get_addr(0x34, 184), format=">I", size=4),
            # TODO: add other PMs...
        )

        # MEDIA_LANE_LINK_PM block corresponds to all the coherent PMs in C-CMIS spec reported in Page 35h. 
        self.MEDIA_LANE_LINK_PM = RegGroupField(consts.MEDIA_LANE_LINK_PM,
            NumberRegField(consts.RX_AVG_CD_PM, get_addr(0x35, 128), format=">i", size=4),
            NumberRegField(consts.RX_MIN_CD_PM, get_addr(0x35, 132), format=">i", size=4),
            NumberRegField(consts.RX_MAX_CD_PM, get_addr(0x35, 136), format=">i", size=4),
            NumberRegField(consts.RX_AVG_DGD_PM, get_addr(0x35, 140), format=">H", size=2, scale=100.0),
            NumberRegField(consts.RX_MIN_DGD_PM, get_addr(0x35, 142), format=">H", size=2, scale=100.0),
            NumberRegField(consts.RX_MAX_DGD_PM, get_addr(0x35, 144), format=">H", size=2, scale=100.0),   
            NumberRegField(consts.RX_AVG_SOPMD_PM, get_addr(0x35, 146), format=">H", size=2, scale=100.0),
            NumberRegField(consts.RX_MIN_SOPMD_PM, get_addr(0x35, 148), format=">H", size=2, scale=100.0),
            NumberRegField(consts.RX_MAX_SOPMD_PM, get_addr(0x35, 150), format=">H", size=2, scale=100.0),
            NumberRegField(consts.RX_AVG_PDL_PM, get_addr(0x35, 152), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MIN_PDL_PM, get_addr(0x35, 154), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MAX_PDL_PM, get_addr(0x35, 156), format=">H", size=2, scale=10.0), 
            NumberRegField(consts.RX_AVG_OSNR_PM, get_addr(0x35, 158), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MIN_OSNR_PM, get_addr(0x35, 160), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MAX_OSNR_PM, get_addr(0x35, 162), format=">H", size=2, scale=10.0), 
            NumberRegField(consts.RX_AVG_ESNR_PM, get_addr(0x35, 164), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MIN_ESNR_PM, get_addr(0x35, 166), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MAX_ESNR_PM, get_addr(0x35, 168), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_AVG_CFO_PM, get_addr(0x35, 170), format=">h", size=2),
            NumberRegField(consts.RX_MIN_CFO_PM, get_addr(0x35, 172), format=">h", size=2),
            NumberRegField(consts.RX_MAX_CFO_PM, get_addr(0x35, 174), format=">h", size=2),
            NumberRegField(consts.RX_AVG_EVM_PM, get_addr(0x35, 176), format=">H", size=2, scale=655.35),
            NumberRegField(consts.RX_MIN_EVM_PM, get_addr(0x35, 178), format=">H", size=2, scale=655.35),
            NumberRegField(consts.RX_MAX_EVM_PM, get_addr(0x35, 180), format=">H", size=2, scale=655.35),
            NumberRegField(consts.TX_AVG_POWER_PM, get_addr(0x35,182), format=">h", size=2, scale=100.0),
            NumberRegField(consts.TX_MIN_POWER_PM, get_addr(0x35,184), format=">h", size=2, scale=100.0),
            NumberRegField(consts.TX_MAX_POWER_PM, get_addr(0x35,186), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_AVG_POWER_PM, get_addr(0x35,188), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_MIN_POWER_PM, get_addr(0x35,190), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_MAX_POWER_PM, get_addr(0x35,192), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_AVG_POWER_PM, get_addr(0x35,188), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_MIN_POWER_PM, get_addr(0x35,190), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_MAX_POWER_PM, get_addr(0x35,192), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_AVG_SIG_POWER_PM, get_addr(0x35,194), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_MIN_SIG_POWER_PM, get_addr(0x35,196), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_MAX_SIG_POWER_PM, get_addr(0x35,198), format=">h", size=2, scale=100.0),
            NumberRegField(consts.RX_AVG_SOPROC_PM, get_addr(0x35,200), format=">H", size=2),
            NumberRegField(consts.RX_MIN_SOPROC_PM, get_addr(0x35,202), format=">H", size=2),
            NumberRegField(consts.RX_MAX_SOPROC_PM, get_addr(0x35,204), format=">H", size=2),
            NumberRegField(consts.RX_AVG_MER_PM, get_addr(0x35,206), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MIN_MER_PM, get_addr(0x35,208), format=">H", size=2, scale=10.0),
            NumberRegField(consts.RX_MAX_MER_PM, get_addr(0x35,210), format=">H", size=2, scale=10.0),
            # TODO: add others PMs...
        )

        self.TRANS_CONFIG = RegGroupField(consts.TRANS_CONFIG_FIELD,
            NumberRegField(consts.MODULE_LEVEL_CONTROL, get_addr(0x0, 26), size=1, ro=False),
        )

        self.TRANS_CDB = RegGroupField(consts.TRANS_CDB_FIELD,
            NumberRegField(consts.CDB_SUPPORT, get_addr(0x01, 163), size=1),
            NumberRegField(consts.CDB_SEQ_WRITE_LENGTH_EXT, get_addr(0x01, 164), size=1),
            NumberRegField(consts.CDB_RPL_LENGTH, get_addr(0x9f, 134), size=1, ro=False),
            NumberRegField(consts.CDB_RPL_CHKCODE, get_addr(0x9f, 135), size=1, ro=False),
            ListRegField(consts.CDB_LPL, get_addr(0x9f, 136), format='120B', size=120, ro=False),
            ListRegField(consts.CDB_CMD, get_addr(0x9f, 128), format='2B', size=2, ro=False),
            ListRegField(consts.CDB_WRITE_MSG, get_addr(0x9f, 130), format='126B', size=126, ro=False),
        )
        # TODO: add remaining fields
