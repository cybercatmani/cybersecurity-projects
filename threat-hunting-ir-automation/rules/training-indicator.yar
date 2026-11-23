rule SOC_Lab_Benign_Training_Marker {
 meta:
  description = "Harmless unique marker in lab fixture; not malware detection"
  author = "Threat Hunting Learning Lab"
 strings:
  $marker = "SOC_LAB_TRAINING_MARKER_2026" ascii
 condition:
  $marker
}
