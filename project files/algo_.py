def cmp_address(d_1,d_2):
	if d_1['country']!=d_2['country']:
		return "Wrong"
	else:
		if d_1['state']!=d_2['state']:
			return "same country "
		else:
			if d_1['city']!=d_2['city']:
				return "same state"
			else:
				if d_1['address']!=d_2['address']:
					return "same city"
				else:
					return "correct"


