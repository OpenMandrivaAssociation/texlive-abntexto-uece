%global tl_name abntexto-uece
%global tl_revision 76157

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX class for formatting academic papers in UECE standards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abntexto-uece
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto-uece.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto-uece.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a unofficial LaTeX class created for Brazilian students to
facilitate the use of standards from the Universidade Estadual do Ceara
(UECE) in academic works like TCCs, dissertations, and theses.

