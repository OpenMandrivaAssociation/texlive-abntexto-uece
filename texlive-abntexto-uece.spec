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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a unofficial LaTeX class created for Brazilian students to
facilitate the use of standards from the Universidade Estadual do Ceara
(UECE) in academic works like TCCs, dissertations, and theses.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/abntexto-uece
%dir %{_datadir}/texmf-dist/tex/latex/abntexto-uece
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/CHANGELOG
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/README.md
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/abntexto-uece-exemplo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/abntexto-uece-exemplo.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/abntexto-uece.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/abntexto-uece.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntexto-uece/abntexto-uece.tex
%{_datadir}/texmf-dist/tex/latex/abntexto-uece/abntexto-uece.cls
