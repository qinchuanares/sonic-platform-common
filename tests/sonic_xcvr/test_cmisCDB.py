from mock import MagicMock
import pytest
from sonic_platform_base.sonic_xcvr.api.public.cmis import CmisApi
from sonic_platform_base.sonic_xcvr.api.public.cmisCDB import CmisCdbApi
from sonic_platform_base.sonic_xcvr.mem_maps.public.cmis import CmisMemMap
from sonic_platform_base.sonic_xcvr.xcvr_eeprom import XcvrEeprom
from sonic_platform_base.sonic_xcvr.codes.public.sff8024 import Sff8024
from sonic_platform_base.sonic_xcvr.codes.public.cmis import CmisCodes

class TestCDB(object):
    codes = CmisCodes
    mem_map = CmisMemMap(codes)
    reader = MagicMock(return_value=None)
    writer = MagicMock()
    eeprom = XcvrEeprom(reader, writer, mem_map)
    api = CmisCdbApi(eeprom)

    @pytest.mark.parametrize("mock_response, expected", [
        (64, False),
        (0, True)
    ])
    def test_cdb1_chkflags(self, mock_response, expected):
        self.api.xcvr_eeprom.read = MagicMock()
        self.api.xcvr_eeprom.read.return_value = mock_response
        result = self.api.cdb1_chkflags()
        assert result == expected


    @pytest.mark.parametrize("input_param, expected", [
        (bytearray(b'\x00'), 255)
    ])
    def test_cdb_chkcode(self, input_param, expected):
        result = self.api.cdb_chkcode(input_param)
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([1], 1),
        ([128,128,128], 128)
    ])
    def test_cdb1_chkstatus(self, mock_response, expected):
        self.api.xcvr_eeprom.read = MagicMock()
        self.api.xcvr_eeprom.read.side_effect = mock_response
        result = self.api.cdb1_chkstatus()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        (
            [18, 35, (0, 7, 112, 255, 255, 16, 0, 0, 19, 136, 0, 100, 3, 232, 19, 136, 58, 152)],
            (18, 35, (0, 7, 112, 255, 255, 16, 0, 0, 19, 136, 0, 100, 3, 232, 19, 136, 58, 152))
        )
    ])
    def test_read_cdb(self, mock_response, expected):
        self.api.xcvr_eeprom.read = MagicMock()
        self.api.xcvr_eeprom.read.side_effect = mock_response[0:2]
        self.api.xcvr_eeprom.read_raw = MagicMock()
        self.api.xcvr_eeprom.read_raw.return_value = mock_response[2]
        result = self.api.read_cdb()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([[1], (None, None, None)], (None, None, None)),
        ([[128, 128, 128], (None, None, None)], (None, None, None)),
    ])
    def test_cmd0000h(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response[0]
        self.api.read_cdb = MagicMock()
        self.api.read_cdb.return_value = mock_response[1]
        result = self.api.cmd0000h()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([1], 1),
        ([128, 128, 64], 64)
    ])
    def test_cmd0001h(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.cmd0001h()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([[1], (None, None, None)], (None, None, None)),
        ([[64, 64, 64], (None, None, None)], (None, None, None)),
    ])
    def test_cmd0040h(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response[0]
        self.api.read_cdb = MagicMock()
        self.api.read_cdb.return_value = mock_response[1]
        result = self.api.cmd0040h()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([[1], (None, None, None)], (None, None, None)),
        ([[64, 64, 64], (None, None, None)], (None, None, None)),
    ])
    def test_get_fw_management_features(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response[0]
        self.api.read_cdb = MagicMock()
        self.api.read_cdb.return_value = mock_response[1]        
        result = self.api.get_fw_management_features()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([[1], (None, None, None)], (None, None, None)),
        ([[64, 64, 64], (None, None, None)], (None, None, None)),
    ])
    def test_get_fw_info(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response[0]
        self.api.read_cdb = MagicMock()
        self.api.read_cdb.return_value = mock_response[1]
        result = self.api.get_fw_info()
        assert result == expected

    @pytest.mark.parametrize("input_param, mock_response, expected", [
        ([3, bytearray(b'\x00\x00\x00'), 1000000], [1], 1),
        ([3, bytearray(b'\x00\x00\x00'), 1000000], [64, 64, 64], 64)
    ])
    def test_start_fw_download(self, input_param, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.start_fw_download(*input_param)
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([1], 1),
        ([64, 64, 64], 64),
    ])
    def test_abort_fw_download(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.abort_fw_download()
        assert result == expected

    @pytest.mark.parametrize("input_param, mock_response, expected", [
        ([100, bytearray(116)], [1], 1),
        ([100, bytearray(116)], [64, 64, 64], 64)
    ])
    def test_block_write_lpl(self, input_param, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.block_write_lpl(*input_param)
        assert result == expected

    @pytest.mark.parametrize("input_param, mock_response, expected", [
        ([100, bytearray(2048), True, 100], [1], 1),
        ([100, bytearray(2047), False, 100], [64, 64, 64], 64),
    ])
    def test_block_write_epl(self, input_param, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.block_write_epl(*input_param)
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([1], 1),
        ([64, 64, 64], 64),
    ])
    def test_validate_fw_image(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.validate_fw_image()
        assert result == expected

    @pytest.mark.parametrize("mock_response, expected", [
        ([1], 1),
        ([64, 64, 64], 64),
    ])
    def test_run_fw_image(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.run_fw_image()
        assert result == expected
        
    @pytest.mark.parametrize("mock_response, expected", [
        ([1], 1),
        ([64, 64, 64], 64),
    ])
    def test_commit_fw_image(self, mock_response, expected):
        self.api.cdb1_chkstatus = MagicMock()
        self.api.cdb1_chkstatus.side_effect = mock_response
        result = self.api.commit_fw_image()
        assert result == expected
