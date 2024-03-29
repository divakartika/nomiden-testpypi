# nomiden

![nomiden code example](https://raw.githubusercontent.com/divakartika/nomiden-testpypi/main/images/nomiden3.png)

## What is it?

**nomiden** is a Python package that provides information extraction from Indonesian ID Numbers, i.e. personal ID number NIK (Nomor Induk Kependudukan) and family ID number KK (Kartu Keluarga). This package is intended to help users dealing with population and client data to auto-complete missing data or add valuable information, given the ID numbers. Information regarding identity numbers refers to Article 33 of Government Regulation Number 37 of 2007 (Pasal 37 PP Nomor 37 Tahun 2007).

## Main Features
Here are the things that **nomiden** can do for you:

  - Retreive regional information 
    - Province
    - City
    - District
  - Retreive gender information (NIK only)
  - Retreive birth information (NIK only)
    - Age
    - Birthday (e.g. 15 June 2000)
    - Birth date
    - Birth month
    - Birth year
    - Birth in datetime
  - Retreive registration information (KK only)
    - Registration day (e.g. 15 June 2000)
    - Registration date
    - Registration month
    - Registration year
    - Registration in datetime
  - Registration order
  - Complete information in a dictionary

## Where to get it
The source code is currently hosted on GitHub at: [https://github.com/divakartika/nomiden-testpypi](https://github.com/divakartika/nomiden-testpypi)

**nomiden** is available at the [Test Python Package Index (Test PyPI)](https://test.pypi.org/project/nomiden/).

```sh
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple nomiden
```

## Dependencies
- [Pandas - Supports data-related operations](https://pandas.pydata.org)

## License
[MIT](LICENSE)

## Documentation
[https://nomiden-testpypi.readthedocs.io](https://nomiden-testpypi.readthedocs.io) 

## Data Source
Region code data used in this package is retrieved from [kodewilayah](https://github.com/kodewilayah/permendagri-72-2019) based on the Regulation of the Minister of Home Affairs number 72 of 2019 (Permendagri No. 72 tahun 2019).

## Getting Help & Discussion

For usage questions and development discussions, feel free to contact diva@algorit.ma.