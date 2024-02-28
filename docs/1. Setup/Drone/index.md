---
title: Home
---

# GEMINI Data Center

Genomics X Environment X Management Innovation in Intelligence for Climate Adaptation

Your all-in-one resource for managing data for large-scale breeding trials.

/// tab | User Docs

## Modules

Navigate to the included modules using the icons on the sidebar. Visit the following pages for more information

[Upload](upload.md)

: Upload image data, GCP locations, and other metadata

[Process](process.md)

: View available data for a given trial and generate orthomosaics, plot boundaries, and aerial and ground-based sensor traits

[Table](table.md)

: **Coming Soon** View traits and field information in a tabular layout

[Map](map.md)

: View traits and field information on a map

[Query](query.md)

: Retrieve images from ground-based sensors based on accesssion, plot number, or plot row/column pairs

///

/// tab | Developer Docs

## Page Components

The main content section of the page is set to conditionally display either the components responsible for each section in the sidebar or, if no module is selected, the splash page will be displayed.

All assets for the splash page are located in the `public` directory.

## Sidebar

The CollapsibleSidebar is the main method of navigating the app. The icons with their labels set the state variables necessary to change the main content section of the page. Additionally, within the `Components/Menu/CollapsibleSidebar` component, the selection menus for viewing and processing data are reached, and in the case of the data viewing component, this is also where props are passed (props for the data processing component are derived from the central state managed by the Context API).

///
