#!/bin/bash

# ============================================
# Script Name  : reset.sh
# Author       : Aromal
# Description  : Resets Phoenix tool configurations
#                and optionally deletes reports
# Version      : 1.0.2
# ============================================

echo "1. Hard Reset - Resets config and deletes the reports"
echo "2. Soft Reset - Resets only the config"

read -p "Enter your option: " option

if [ $option -eq 1 ]; then
        python -m reset.reset_config
        rm -rf ./generated
else
        python -m reset.reset_config
fi