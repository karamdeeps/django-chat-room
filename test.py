import requests
import json

url = "http://localhost:8000/transaction/api/parking"

data = {'entry_lane_id': 23, 'exit_lane_id': 24,
        'plaza_id': 6, 'epc_id': '34161FA82032897213C82460',
        't_id': 'E4161FA82032897213C82460', 'toll_amount': 90.0,
        'ticket_id': '09456456892512359', 'transaction_date_time': 1600077240.0,
        'tag_read_date_time': 1600077240.0, 'entry_transaction_date_time': 1600058700.0,
        'fastag_user_memory_data': '5a7272436a390993595819fc0533c9198f90bd6efbb34251c78cda299cb8ba',
        'fastag_is_signature_verified': True, 'fastag_tag_vc': '0400',
        'fastag_rfu': 'sdfjsd', 'fastag_tag_vrn': '585858585858585858585858',
        'lp_number': 'up16', 'avc_vehicle_classification': '0400'}

requests.post(url=url, data=data)
