#Makefile at top of application tree
TOP = .
include $(TOP)/configure/CONFIG
DIRS := $(DIRS) configure
DIRS := $(DIRS) pslApp
ifeq ($(BUILD_IOCS), YES)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocs))
iocs_DEPEND_DIRS += pslApp
endif
# Comment out the following lines to disable creation of example iocs and documentation
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard etc))

ifeq ($(wildcard etc),etc)
	include $(TOP)/etc/makeIocs/Makefile.iocs
	UNINSTALL_DIRS += $(IOC_DIRS)
endif

include $(TOP)/configure/RULES_TOP

uninstall: uninstall_iocs
uninstall_iocs:
	$(MAKE) -C iocs uninstall
.PHONY: uninstall uninstall_iocs

realuninstall: realuninstall_iocs
realuninstall_iocs:
	$(MAKE) -C iocs realuninstall
.PHONY: realuninstall realuninstall_iocs

