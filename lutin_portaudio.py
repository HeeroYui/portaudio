#!/usr/bin/python
import lutinModule as module
import lutinTools as tools
import lutinDebug as debug

def get_desc():
	return "portaudio : Audio wrapper interface"

def create(target):
	myModule = module.Module(__file__, 'portaudio', 'LIBRARY')
	
	myModule.add_src_file([
		'src/common/pa_allocation.c',
		'src/common/pa_converters.c',
		'src/common/pa_cpuload.c',
		'src/common/pa_dither.c',
		'src/common/pa_debugprint.c',
		'src/common/pa_front.c',
		'src/common/pa_process.c',
		'src/common/pa_stream.c',
		'src/common/pa_trace.c',
		'src/hostapi/skeleton/pa_hostapi_skeleton.c',
		'src/hostapi/alsa/pa_linux_alsa.c',
		'src/hostapi/jack/pa_jack.c',
		'src/hostapi/oss/pa_unix_oss.c',
		'src/common/pa_ringbuffer.c',
		'src/os/unix/pa_unix_hostapis.c',
		'src/os/unix/pa_unix_util.c'
		])
	
	myModule.compile_flags_CC([
		'-DPA_LITTLE_ENDIAN',
		'-DPACKAGE_NAME=\"\"',
		'-DPACKAGE_TARNAME=\"\"',
		'-DPACKAGE_VERSION=\"\"',
		'-DPACKAGE_STRING=\"\"',
		'-DPACKAGE_BUGREPORT=\"\"',
		'-DPACKAGE_URL=\"\"',
		'-DSTDC_HEADERS=1',
		'-DHAVE_SYS_TYPES_H=1',
		'-DHAVE_SYS_STAT_H=1',
		'-DHAVE_STDLIB_H=1',
		'-DHAVE_STRING_H=1',
		'-DHAVE_MEMORY_H=1',
		'-DHAVE_STRINGS_H=1',
		'-DHAVE_INTTYPES_H=1',
		'-DHAVE_STDINT_H=1',
		'-DHAVE_UNISTD_H=1',
		'-DHAVE_DLFCN_H=1',
		'-DLT_OBJDIR=\".libs/\"',
		'-DHAVE_SYS_SOUNDCARD_H=1',
		'-DHAVE_LINUX_SOUNDCARD_H=1',
		'-DSIZEOF_SHORT=2',
		'-DSIZEOF_INT=4',
		'-DSIZEOF_LONG=8',
		'-DHAVE_CLOCK_GETTIME=1',
		'-DHAVE_NANOSLEEP=1'
		])
	
	myModule.compile_version_CC(1999)
	
	myModule.add_optionnal_module_depend('alsa', "PA_USE_ALSA=1")
	myModule.add_optionnal_module_depend('jack', "PA_USE_JACK=1")
	myModule.add_optionnal_module_depend('oss', "PA_USE_OSS=1")
	
	myModule.add_module_depend(['audio', 'airtaudio', 'drain', 'ejson'])
	myModule.add_export_path(tools.get_current_path(__file__) + '/include')
	myModule.add_path(tools.get_current_path(__file__)+"/src/common")
	myModule.add_path(tools.get_current_path(__file__)+"/src/os/unix")
	
	# add the currrent module at the 
	return myModule


